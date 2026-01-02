# app/vectorstore/chroma.py

from langchain_community.vectorstores import Chroma
from app.ingestion.embeddings import get_embedding_model

def get_vectorstore(collection_name="default"):
    return Chroma(
        persist_directory="db",
        embedding_function=get_embedding_model(),
        collection_name=collection_name
    )
