from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from app.models.responses import NormalizedTerm
from app.models.evidence import RetrievedEvidence

class IntelligenceInput(BaseModel):
    analysis_id: str
    innovation_name: str
    innovation_description: str
    product_type: str
    product_form: Optional[str] = None
    intended_use: Optional[str] = None
    claims: Optional[List[str]] = None
    ingredients: List[str]
    normalized_ingredients: List[NormalizedTerm]
    biological_resources: Optional[List[str]] = None
    resource_source_information: Optional[Dict[str, Any]] = None
    formulation_context: Optional[Dict[str, Any]] = None
    manufacturing_information: Optional[Dict[str, Any]] = None
    labelling_information: Optional[Dict[str, Any]] = None
    jurisdiction: str
    detected_language: str
    output_language: str
    retrieved_evidence: List[RetrievedEvidence]
