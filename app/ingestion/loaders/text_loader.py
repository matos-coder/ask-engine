from langchain.schema import Document
from app.ingestion.normalizer import normalize_text

def load_text(text: str, source="manual"):
    return [
        Document(
            page_content=normalize_text(text),
            metadata={"source": source}
        )
    ]
