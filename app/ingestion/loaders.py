# app/ingestion/loaders.py

from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredURLLoader,
    Docx2txtLoader
)

def load_pdf(path):
    return PyPDFLoader(path).load()

def load_docx(path):
    return Docx2txtLoader(path).load()

def load_url(url):
    return UnstructuredURLLoader(urls=[url]).load()

def load_text(text):
    return [{"page_content": text}]
