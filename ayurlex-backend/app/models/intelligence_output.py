from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from app.models.evidence import RetrievedEvidence

class ConfidenceIndicator(BaseModel):
    score: float
    level: str
    explanation: str
    limitations: List[str]

class ClassificationOutput(BaseModel):
    type: str
    label: str
    summary: str

class ModuleOutput(BaseModel):
    module: str
    status: str
    classification: Optional[ClassificationOutput] = None
    signals: List[str]
    summary: str
    evidence_ids: List[str]
    confidence: float
    limitations: List[str]
    recommended_actions: List[str]

class PatentContextOutput(BaseModel):
    status: str
    signals: List[str]
    evidence_ids: List[str]

class PriorArtOutput(BaseModel):
    status: str
    similarity_signals: List[str]
    evidence_ids: List[str]

class DifferentiationOutput(BaseModel):
    signals: List[str]
    evidence_ids: List[str]

class TrademarkContextOutput(BaseModel):
    status: str
    signals: List[str]

class IPModuleOutput(BaseModel):
    module: str
    status: str
    summary: str
    patent_context: PatentContextOutput
    prior_art: PriorArtOutput
    innovation_differentiation: DifferentiationOutput
    trademark_context: TrademarkContextOutput
    key_findings: List[str]
    supporting_evidence: List[RetrievedEvidence]
    confidence: float
    limitations: List[str]
    recommended_actions: List[str]

class TKTermAnalysis(BaseModel):
    normalized_terms: List[str]
    ambiguous_terms: List[str]

class TKIngredientAnalysis(BaseModel):
    ingredient: str
    traditional_context: str
    evidence_ids: List[str]
    confidence: float

class TKFormulationAnalysis(BaseModel):
    signals: List[str]
    evidence_ids: List[str]

class TKUseAnalysis(BaseModel):
    signals: List[str]
    evidence_ids: List[str]

class TKModuleOutput(BaseModel):
    module: str
    status: str
    summary: str
    term_analysis: TKTermAnalysis
    ingredient_analysis: List[TKIngredientAnalysis]
    formulation_analysis: TKFormulationAnalysis
    traditional_use_analysis: TKUseAnalysis
    key_findings: List[str]
    supporting_evidence: List[RetrievedEvidence]
    confidence: ConfidenceIndicator
    limitations: List[str]
    recommended_actions: List[str]

class ABSResourceAnalysis(BaseModel):
    ingredient: str
    normalized_name: str
    resource_context: str
    available_source_information: str
    signals: List[str]
    evidence_ids: List[str]
    confidence: ConfidenceIndicator

class ABSModuleOutput(BaseModel):
    module: str
    status: str
    summary: str
    context_level: str
    resource_analysis: List[ABSResourceAnalysis]
    utilization_context: Dict[str, Any]
    jurisdiction_context: Dict[str, Any]
    signals: List[Dict[str, Any]]
    supporting_evidence: List[RetrievedEvidence]
    missing_information: List[str]
    confidence: ConfidenceIndicator
    limitations: List[str]
    recommended_actions: List[str]

class ProductClassificationOutput(BaseModel):
    potential_contexts: List[str]
    signals: List[str]
    confidence: ConfidenceIndicator

class IngredientRegulatoryAnalysis(BaseModel):
    ingredient: str
    normalized_name: str
    scientific_name: Optional[str] = None
    regulatory_context: str
    signals: List[str]
    evidence_ids: List[str]
    confidence: ConfidenceIndicator

class RegulatorySignal(BaseModel):
    signal: str
    priority: str
    explanation: str
    evidence_ids: List[str]
    confidence: float

class RegulatoryModuleOutput(BaseModel):
    module: str
    status: str
    summary: str
    product_classification: ProductClassificationOutput
    claim_analysis: Dict[str, Any]
    ingredient_analysis: List[IngredientRegulatoryAnalysis]
    product_form_context: Dict[str, Any]
    manufacturing_context: Dict[str, Any]
    labelling_context: Dict[str, Any]
    jurisdiction_context: Dict[str, Any]
    signals: List[RegulatorySignal]
    supporting_evidence: List[RetrievedEvidence]
    missing_information: List[str]
    confidence: ConfidenceIndicator
    limitations: List[str]
    recommended_actions: List[str]

class CoreIntelligenceOutput(BaseModel):
    analysis_id: str
    status: str
    processing: Dict[str, str]
    formulation_intelligence: ModuleOutput
    ip_intelligence: IPModuleOutput
    traditional_knowledge: TKModuleOutput
    abs_context: ABSModuleOutput
    regulatory_context: RegulatoryModuleOutput
    key_findings: List[str]
    evidence: List[RetrievedEvidence]
    confidence: ConfidenceIndicator
    limitations: List[str]
    recommended_next_steps: List[str]
