from pydantic import BaseModel
from typing import List, Optional

class TKEvidenceContext(BaseModel):
    evidence_id: str
    source_title: str
    category: str
    language: str
    source_language: str
    jurisdiction: str
    relevant_excerpt: str
    relevance_score: float
