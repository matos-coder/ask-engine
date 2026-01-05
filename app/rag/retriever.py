from app.vectorstore.chroma import get_vectorstore


def retrieve_context(question: str, client_id: str, k: int = 3) -> str:
    db = get_vectorstore(client_id)

    docs = db.similarity_search(question, k=k)

    if not docs:
        return ""

    return "\n\n".join(d.page_content for d in docs)
