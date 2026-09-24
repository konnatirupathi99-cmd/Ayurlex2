from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class NormalizedTerm(BaseModel):
    user_input: str
    normalized: str
    scientific: Optional[str] = None
    english: Optional[str] = None

class EvidenceSource(BaseModel):
    source_id: str
    document_id: str
    title: str
    category: str
    language: str
    relevant_text: str
    relevance_score: float

class IntelligenceReport(BaseModel):
    analysis_id: str
    innovation_name: str
    jurisdiction: str
    language: str
    detected_language: str
    summary: str
    normalized_terms: List[NormalizedTerm]
    classical_ayurvedic_rationale: Dict[str, Any]
    contemporary_scientific_evidence: Dict[str, Any]
    product_or_process_novelty: Dict[str, Any]
    jurisdictional_interpretation: Dict[str, Any]
    evidence: List[EvidenceSource]
    confidence: Dict[str, Any]
    recommended_next_steps: List[str]
