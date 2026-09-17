from pydantic import BaseModel
from typing import List, Optional
from app.models.intelligence_output import ClassificationOutput

class FormulationEvidenceContext(BaseModel):
    evidence_id: str
    source_title: str
    category: str
    language: str
    relevant_excerpt: str
    relevance_score: float

class FormulationAnalysisResult(BaseModel):
    status: str
    classification: ClassificationOutput
    signals: List[str]
    supporting_evidence: List[FormulationEvidenceContext]
    confidence_score: float
    confidence_level: str
    confidence_explanation: str
    limitations: List[str]
    recommended_actions: List[str]
