from app.vectorstore.chroma import get_vectorstore


def retrieve_context(question: str, client_id: str, k: int = 3) -> str:
    db = get_vectorstore(client_id)

    #docs = db.similarity_search(question, k=k)
    docs = db.similarity_search_with_score(question, k=k)

    filtered = []
    for doc, score in docs:
        # chroma cosine distance → lower is better
        if score > 0.3:     # you can tune
            continue

        filtered.append(doc.page_content)

    if len(filtered) == 0:
        return ""
        
    return "\n\n".join(filtered)
