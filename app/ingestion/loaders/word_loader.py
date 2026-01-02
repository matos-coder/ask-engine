from langchain.document_loaders import UnstructuredWordDocumentLoader
from app.ingestion.normalizer import normalize_text

def load_word(path: str):
    loader = UnstructuredWordDocumentLoader(path)
    docs = loader.load()

    for doc in docs:
        doc.page_content = normalize_text(doc.page_content)

    return docs
