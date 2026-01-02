import re

def normalize_text(text: str) -> str:
    if not text:
        return ""

    # Normalize newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()
