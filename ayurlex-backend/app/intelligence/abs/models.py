from pydantic import BaseModel
from typing import List

class ABSEvidenceContext(BaseModel):
    evidence_id: str
    source_title: str
    source_type: str
    category: str
    jurisdiction: str
    language: str
    relevant_excerpt: str
    relevance_score: float
