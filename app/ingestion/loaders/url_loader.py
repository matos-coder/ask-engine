from langchain.document_loaders import WebBaseLoader
from app.ingestion.normalizer import normalize_text

def load_url(url: str):
    loader = WebBaseLoader(url)
    docs = loader.load()

    for doc in docs:
        doc.page_content = normalize_text(doc.page_content)

    return docs
