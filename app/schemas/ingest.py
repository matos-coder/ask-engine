from pydantic import BaseModel
from typing import Optional, List

class IngestRequest(BaseModel):
    client_id: str
    urls: Optional[List[str]] = None
    texts: Optional[List[str]] = None
