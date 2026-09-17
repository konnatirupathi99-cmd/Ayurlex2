from pydantic import BaseModel
from typing import List, Optional

class IPEvidenceContext(BaseModel):
    evidence_id: str
    source_title: str
    category: str
    language: str
    jurisdiction: str
    relevant_excerpt: str
    relevance_score: float
