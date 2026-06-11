import streamlit as st
import os
from document_loader import load_and_split_docs
from vector_store import create_vector_store
from rag_pipeline import run_rag_pipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="Self-Healing RAG", layout="wide")
st.title("🛡️ Self-Healing RAG Pipeline")

with st.sidebar:
    st.header("Settings")
    key = st.text_input("Groq API Key", type="password")
    threshold = st.slider("Threshold (Suggestion Trigger)", 0.0, 1.0, 0.7)

up = st.file_uploader("Upload Resume/Document", type=["pdf", "txt"])

if up and key:
    data_dir = os.path.join(BASE_DIR, "data")
    os.makedirs(data_dir, exist_ok=True)

    path = os.path.join(data_dir, up.name)

    with open(path, "wb") as f:
        f.write(up.getbuffer())

    if st.button("Process Document"):
        with st.spinner("Indexing..."):
            docs = load_and_split_docs(path)
            create_vector_store(docs)
            st.success("Vector Store Ready!")

q = st.text_input("Ask a question:")

if q and key:
    with st.spinner("Running Pipeline..."):
        ans, sources, acts, score, suggestions = run_rag_pipeline(
            q,
            key.strip(),
            threshold
        )

    st.markdown(f"### Answer\n{ans}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Confidence Score", f"{score * 100:.1f}%")

    with col2:
        st.write("**Healing Actions:**")
        for a in acts:
            st.write(f"✓ {a}")

    if suggestions:
        st.markdown("### 💡 Suggested Better Questions")
        for sug in suggestions:
            st.markdown(f"- {sug}")

    with st.expander("Sources & Citations"):
        for d, s in sources:
            st.write(f"**Similarity Score: {s:.2f}**")
            st.info(d.page_content[:300] + "...")