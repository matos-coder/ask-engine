from fastapi import HTTPException
from rich import _console
from app.rag.prompt_builder import build_prompt
from app.rag.retriever import retrieve_context
from app.repositories.client_repo import get_client, update_conversation_summary
from app.vectorstore.chroma import get_vectorstore
from app.rag.prompt import STRICT_PROMPT
from app.core.llm import get_llm
from app.core.client_settings import get_client_settings
from db.session import get_db


def answer_question(question: str, client_id: str):
    db = next(get_db())

    client = get_client(db, client_id)

    if not client:
        raise HTTPException(status_code=404, detail="Client not found")


    llm = get_llm()

    context = retrieve_context(
        question=question,
        client_id=client_id
    )
    
    if not context or context.strip() == "":
        settings = get_client_settings(client_id)
        return {"answer": no_answer_response(settings)}


    prompt = build_prompt(
        system_prompt=client.system_prompt,
        conversation_summary=client.conversation_summary,
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    if client.memory_enabled:
        summary_prompt = f"""
Summarize the conversation briefly for future context.

Previous summary:
{client.conversation_summary}

New exchange:
User: {question}
Assistant: {response.content}
"""
        summary = llm.invoke(summary_prompt).content
        update_conversation_summary(db, client, summary)

    return {
        "answer": response.content
    }


def no_answer_response(settings):
    if settings.enable_agent_handoff:
        return (
            "I don't have that information. "
            + settings.handoff_message
        )
    return "I don't have that information."

def llm_answer(context: str, question: str) -> str:
    llm = get_llm()

    prompt = STRICT_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)
    return response.content
