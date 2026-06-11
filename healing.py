class SelfHealer:
    def rewrite_query(self, client, query):
        prompt = f"Rewrite this search query to be more descriptive for vector retrieval: {query}. Output ONLY the rewritten query."
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip()

    def generate_suggestions(self, client, query, context):
        prompt = f"""Original Question: {query}\nContext Snippet: {context[:500]}\n\nBased on the question and context, generate 3 better, more specific versions of the question that would help a RAG system find a more accurate answer.\nOutput ONLY the 3 questions as a bulleted list starting with '-'. No preamble."""
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip().split('\n')

    def check_grounding(self, client, context, answer):
        prompt = f"Context: {context}\n\nAnswer: {answer}\n\nDoes the context support this answer? Reply only YES or NO."
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return "YES" in completion.choices[0].message.content.upper()