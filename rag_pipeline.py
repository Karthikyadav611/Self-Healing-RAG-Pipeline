import os
import numpy as np
from groq import Groq
from healing import SelfHealer
from logger import log_query
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "vectorstore")


def normalize_score(score):
    """
    FAISS relevance score should usually be between 0 and 1.
    1 = best match, 0 = weak match.
    """
    try:
        return float(np.clip(score, 0, 1))
    except Exception:
        return 0.0


def run_rag_pipeline(user_query, api_key, threshold=0.7):
    if not os.path.exists(os.path.join(INDEX_PATH, "index.faiss")):
        return (
            "No documents found. Please upload and process a document in the sidebar first!",
            [],
            ["No Vector Store Found"],
            0,
            []
        )

    client = Groq(api_key=api_key.strip())
    healer = SelfHealer()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    actions = []
    suggestions = []

    docs_scores = vector_db.similarity_search_with_relevance_scores(
        user_query,
        k=5
    )

    top_score = normalize_score(docs_scores[0][1]) if docs_scores else 0.0

    search_query = user_query

    if top_score < threshold:
        actions.append(f"Low confidence ({top_score * 100:.1f}%) detected")

        search_query = healer.rewrite_query(client, user_query)

        docs_scores = vector_db.similarity_search_with_relevance_scores(
            search_query,
            k=5
        )

        top_score = normalize_score(docs_scores[0][1]) if docs_scores else 0.0

        actions.append("Internal query rewrite performed")

        context_for_sugg = "\n".join(
            [doc.page_content for doc, score in docs_scores[:2]]
        ) if docs_scores else ""

        suggestions = healer.generate_suggestions(
            client,
            user_query,
            context_for_sugg
        )

        actions.append("Suggested better questions generated")

    context = "\n".join([doc.page_content for doc, score in docs_scores])

    gen_prompt = f"""
Answer ONLY using the given context.
If the answer is not present in the context, say: "I could not find this information in the uploaded documents."

QUESTION:
{user_query}

CONTEXT:
{context}
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": gen_prompt}]
    )

    answer = res.choices[0].message.content

    if not healer.check_grounding(client, context, answer):
        actions.append("Hallucination check failed - regenerating")

        strict_prompt = "STRICTLY answer only from the context. " + gen_prompt

        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": strict_prompt}]
        )

        answer = res.choices[0].message.content

    log_query(user_query, answer, top_score, actions)

    return answer, docs_scores, actions, top_score, suggestions