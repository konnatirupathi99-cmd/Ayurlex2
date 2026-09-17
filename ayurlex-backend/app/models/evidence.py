from pydantic import BaseModel
from typing import Optional

class RetrievedEvidence(BaseModel):
    evidence_id: str
    source_id: str
    title: str
    category: str  # IP, TK, ABS, Regulatory, etc.
    language: str
    content: str
    relevance_score: float
    jurisdiction: Optional[str] = "International"
