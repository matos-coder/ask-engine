from app.ingestion.splitter import split_documents
from app.vectorstore.chroma import get_vectorstore

def ingest_documents(documents, client_id: str):
    """
    Full ingestion pipeline:
    - split
    - embed
    - store per client
    """

    chunks = split_documents(documents)

    # Attach client info
    for chunk in chunks:
        chunk.metadata["client_id"] = client_id

    vectorstore = get_vectorstore(client_id)
    vectorstore.add_documents(chunks)

    return len(chunks)
