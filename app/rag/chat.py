# app/rag/chat.py

from langchain_groq import ChatGroq
from app.vectorstore.chroma import get_vectorstore
from app.rag.prompt import STRICT_PROMPT

def answer_question(question, collection="default"):
    db = get_vectorstore(collection)
    docs = db.similarity_search(question, k=3)

    if not docs:
        return "I don't have that information."

    context = "\n".join([d.page_content for d in docs])

    llm = ChatGroq(
        model_name="llama3-8b-8192",
        temperature=0
    )

    prompt = STRICT_PROMPT.format(
        context=context,
        question=question
    )

    return llm.invoke(prompt).content
