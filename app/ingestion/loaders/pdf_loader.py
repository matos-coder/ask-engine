from langchain.document_loaders import PyPDFLoader
from app.ingestion.normalizer import normalize_text

def load_pdf(path: str):
    loader = PyPDFLoader(path)
    docs = loader.load()

    for doc in docs:
        doc.page_content = normalize_text(doc.page_content)

    return docs
