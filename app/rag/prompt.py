# app/rag/prompt.py

STRICT_PROMPT = """
You are a strict assistant.
Answer ONLY using the provided context.
If the answer is not in the context, say:
"I don't have that information."

Context:
{context}

Question:
{question}
"""
