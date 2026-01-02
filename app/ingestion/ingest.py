# app/ingestion/ingest.py

from app.ingestion.loaders import *
from app.ingestion.loaders import load_docx
from app.ingestion.loaders.pdf_loader import load_pdf
from app.ingestion.loaders.text_loader import load_text
from app.ingestion.loaders.url_loader import load_url
from app.ingestion.splitter import split_documents
from app.vectorstore.chroma import get_vectorstore

def ingest(source_type, value, collection="default"):
    if source_type == "pdf":
        docs = load_pdf(value)
    elif source_type == "docx":
        docs = load_docx(value)
    elif source_type == "url":
        docs = load_url(value)
    elif source_type == "text":
        docs = load_text(value)
    else:
        raise ValueError("Unsupported source type")

    chunks = split_documents(docs)
    db = get_vectorstore(collection)
    db.add_documents(chunks)
    db.persist()
