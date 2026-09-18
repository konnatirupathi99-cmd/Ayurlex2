from typing import List, Dict, Any
from app.models.intelligence_input import IntelligenceInput
from app.models.evidence import RetrievedEvidence
from app.models.intelligence_output import (
    RegulatoryModuleOutput, 
    RegulatorySignal
)

from .product_classifier import ProductClassifier
from .claim_analyzer import ClaimAnalyzer
from .ingredient_context_analyzer import IngredientContextAnalyzer
from .product_form_analyzer import ProductFormAnalyzer
from .manufacturing_context import ManufacturingContextAnalyzer
from .labelling_context import LabellingContextAnalyzer
from .jurisdiction_context import JurisdictionContextAnalyzer
from .evidence_evaluator import EvidenceEvaluator
from .confidence_calculator import ConfidenceCalculator

async def analyze_regulatory(input_data: IntelligenceInput, evidence: List[RetrievedEvidence]) -> RegulatoryModuleOutput:
    classifier = ProductClassifier()
    claim_analyzer = ClaimAnalyzer()
    ingredient_analyzer = IngredientContextAnalyzer()
    form_analyzer = ProductFormAnalyzer()
    manufacturing_analyzer = ManufacturingContextAnalyzer()
    labelling_analyzer = LabellingContextAnalyzer()
    jurisdiction_analyzer = JurisdictionContextAnalyzer()
    evidence_evaluator = EvidenceEvaluator()
    confidence_calculator = ConfidenceCalculator()
    
    missing_info = []
    recommended_actions = []
    all_signals_str = []
    structured_signals = []
    
    jurisdiction_res = jurisdiction_analyzer.analyze(input_data.jurisdiction)
    if not input_data.jurisdiction:
        missing_info.append("Jurisdiction not specified.")
    all_signals_str.extend(jurisdiction_res["signals"])
    
    evidence_res = evidence_evaluator.analyze(evidence, jurisdiction_res["context"])
    valid_evidence = evidence_res["valid_evidence"]
    all_signals_str.extend(evidence_res["signals"])
    
    if not input_data.product_type:
        missing_info.append("Product type not provided.")
    if not input_data.innovation_description:
        missing_info.append("Product description not provided.")
    
    classification_res = classifier.analyze(
        input_data.product_type or "", 
        input_data.intended_use or "", 
        input_data.innovation_description or ""
    )
    all_signals_str.extend(classification_res.signals)
    
    if not input_data.claims and not input_data.intended_use:
        missing_info.append("Product claims not provided.")
        missing_info.append("Intended use unclear.")
        
    claim_res = claim_analyzer.analyze(input_data.claims or [], input_data.intended_use or "")
    all_signals_str.extend(claim_res["signals"])
    
    if not input_data.ingredients:
        missing_info.append("Ingredient information incomplete.")
        
    ingredient_res = ingredient_analyzer.analyze(
        input_data.ingredients, 
        input_data.normalized_ingredients, 
        valid_evidence
    )
    
    if not input_data.product_form:
        missing_info.append("Product form not provided.")
        
    form_res = form_analyzer.analyze(input_data.product_form)
    all_signals_str.extend(form_res["signals"])
    
    if not input_data.manufacturing_information:
        missing_info.append("Manufacturing context is unavailable.")
    mfg_res = manufacturing_analyzer.analyze(input_data.manufacturing_information)
    all_signals_str.extend(mfg_res["signals"])
    
    if not input_data.labelling_information:
        missing_info.append("Labelling information not available.")
    labelling_res = labelling_analyzer.analyze(input_data.labelling_information)
    all_signals_str.extend(labelling_res["signals"])
    
    for s in all_signals_str:
        priority = "high" if "REVIEW" in s or "INSUFFICIENT" in s else "medium"
        structured_signals.append(
            RegulatorySignal(
                signal=s.replace(" ", "_"),
                priority=priority,
                explanation=s.title(),
                evidence_ids=[e.evidence_id for e in valid_evidence],
                confidence=0.7
            )
        )
        
    if missing_info:
        recommended_actions.append("Provide missing information to improve analysis accuracy.")
    if "PRODUCT CLASSIFICATION REQUIRES FURTHER REVIEW" in all_signals_str or "MULTIPLE PRODUCT CONTEXTS POSSIBLE" in all_signals_str:
        recommended_actions.append("Clarify product positioning.")
    if "JURISDICTION-SPECIFIC REVIEW RECOMMENDED" in all_signals_str:
        recommended_actions.append("Conduct jurisdiction-specific review with legal specialists.")
        
    confidence = confidence_calculator.calculate(missing_info, len(valid_evidence), all_signals_str)
    
    return RegulatoryModuleOutput(
        module="regulatory_intelligence",
        status="completed" if not missing_info else "needs_review",
        summary="Regulatory context analysis completed. Findings do not constitute product approval guarantees.",
        product_classification=classification_res,
        claim_analysis=claim_res,
        ingredient_analysis=ingredient_res,
        product_form_context=form_res,
        manufacturing_context=mfg_res,
        labelling_context=labelling_res,
        jurisdiction_context=jurisdiction_res,
        signals=structured_signals,
        supporting_evidence=valid_evidence,
        missing_information=missing_info,
        confidence=confidence,
        limitations=confidence.limitations,
        recommended_actions=recommended_actions
    )
