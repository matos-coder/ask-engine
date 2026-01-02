# app/rag/chat.py

from langchain_groq import ChatGroq
from app.vectorstore.chroma import get_vectorstore
from app.rag.prompt import STRICT_PROMPT
from app.settings.client import get_client_settings


def answer_question(question: str, client_id: str = "default"):
    """
    Main RAG entry point.
    """

    # 1. Load tenant/client settings
    settings = get_client_settings(client_id)

    # 2. Load tenant-specific vector DB
    db = get_vectorstore(client_id)

    # 3. Retrieve relevant documents
    docs = db.similarity_search(question, k=3)

    # 4. No context found → fallback
    if not docs:
        return {
            "answer": no_answer_response(settings),
            "handoff": settings.enable_agent_handoff
        }

    # 5. Build context
    context = "\n\n".join(d.page_content for d in docs)

    # 6. Ask LLM
    answer = llm_answer(context, question)

    return {
        "answer": answer,
        "handoff": False  # default: bot only
    }


def llm_answer(context: str, question: str) -> str:
    """
    Handles ONLY LLM interaction.
    """

    llm = ChatGroq(
        model_name="llama3-8b-8192",
        temperature=0
    )

    prompt = STRICT_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)
    return response.content


def no_answer_response(client_settings):
    """
    Handles fallback logic.
    """
    if client_settings.enable_agent_handoff:
        return (
            "I don't have that information. "
            + client_settings.handoff_message
        )

    return "I don't have that information."
