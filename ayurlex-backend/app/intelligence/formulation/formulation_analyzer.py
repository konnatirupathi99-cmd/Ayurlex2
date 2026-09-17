from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.evidence import RetrievedEvidence
from app.models.intelligence_output import ModuleOutput

from app.intelligence.formulation.evidence_evaluator import EvidenceEvaluator
from app.intelligence.formulation.similarity_engine import SimilarityEngine
from app.intelligence.formulation.confidence_calculator import FormulationConfidenceCalculator
from app.intelligence.formulation.classifier import FormulationClassifier

async def analyze_formulation(input_data: IntelligenceInput, evidence: List[RetrievedEvidence]) -> ModuleOutput:
    """
    Formulation Intelligence Engine Orchestrator
    """
    # 1. Evaluate Evidence
    formulation_evidence = EvidenceEvaluator.evaluate(evidence)
    
    # 2. Similarity Engine
    similarity_result = SimilarityEngine.calculate_similarity(input_data.normalized_ingredients, formulation_evidence)
    
    # 3. Calculate Confidence & Detect Limitations
    confidence_data = FormulationConfidenceCalculator.calculate(
        input_data=input_data,
        similarity_score=similarity_result["score"],
        evidence=formulation_evidence
    )
    
    # 4. Classify
    classification = FormulationClassifier.classify(similarity_result, confidence_data["score"])
    
    # Map Signals and Actions based on classification
    signals = [classification.label]
    recommended_actions = []
    status = "completed"
    
    if classification.type == "unclear":
        status = "limited_evidence"
        recommended_actions.append("Provide additional formulation details and review relevant evidence.")
    elif classification.type == "classical":
        recommended_actions.append("Review supporting references and formulation details.")
    elif classification.type == "proprietary":
        recommended_actions.append("Review formulation differentiation and supporting evidence.")
        signals.append("Custom Ingredient Combination")
    elif classification.type == "potentially_novel":
        recommended_actions.append("Conduct detailed prior-art and specialist review.")
    
    return ModuleOutput(
        module="formulation_intelligence",
        status=status,
        classification=classification,
        signals=signals,
        summary=classification.summary,
        evidence_ids=[e.evidence_id for e in formulation_evidence],
        confidence=confidence_data["score"],
        limitations=confidence_data["limitations"],
        recommended_actions=recommended_actions
    )
