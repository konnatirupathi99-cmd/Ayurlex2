from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from app.models.responses import NormalizedTerm
from app.models.evidence import RetrievedEvidence

class IntelligenceInput(BaseModel):
    analysis_id: str
    innovation_name: str
    innovation_description: str
    product_type: str
    ingredients: List[str]
    normalized_ingredients: List[NormalizedTerm]
    jurisdiction: str
    detected_language: str
    output_language: str
    retrieved_evidence: List[RetrievedEvidence]
