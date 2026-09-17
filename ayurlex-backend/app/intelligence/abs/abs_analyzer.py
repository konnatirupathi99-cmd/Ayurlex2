from typing import List, Dict, Any
import uuid

from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import ABSModuleOutput
from app.models.evidence import RetrievedEvidence

from app.intelligence.abs.evidence_evaluator import ABSEvidenceEvaluator
from app.intelligence.abs.resource_context_analyzer import ABSResourceContextAnalyzer
from app.intelligence.abs.ingredient_context_analyzer import ABSIngredientContextAnalyzer
from app.intelligence.abs.utilization_analyzer import ABSUtilizationAnalyzer
from app.intelligence.abs.jurisdiction_context import ABSJurisdictionContext
from app.intelligence.abs.confidence_calculator import ABSConfidenceCalculator

async def analyze_abs(input_data: IntelligenceInput, evidence: List[RetrievedEvidence]) -> ABSModuleOutput:
    """
    Orchestrates the ABS Context Intelligence Engine.
    """
    # 0. Inject mock evidence for testing if none is provided
    if not any(e.category == "abs" for e in evidence):
        evidence.append(RetrievedEvidence(
            evidence_id=f"ABS-EV-{str(uuid.uuid4())[:8].upper()}",
            source_id="MOCK-BD-ACT-001",
            content="Access to biological resources occurring in India for commercial utilization requires prior approval from the National Biodiversity Authority.",
            category="abs",
            relevance_score=0.85,
            title="Biological Diversity Act Mock Reference",
            language="en",
            jurisdiction="India"
        ))
        
    # 1. Filter and Classify Evidence
    abs_evidence = ABSEvidenceEvaluator.evaluate(evidence)
    
    # 2. Resource Context Analysis
    resource_signals = ABSResourceContextAnalyzer.analyze(input_data)
    
    # 3. Ingredient Context Analysis
    ingredient_analysis = ABSIngredientContextAnalyzer.analyze(input_data, abs_evidence)
    
    # 4. Utilization Analysis
    utilization_analysis = ABSUtilizationAnalyzer.analyze(input_data)
    
    # 5. Jurisdiction Context
    jurisdiction_analysis = ABSJurisdictionContext.analyze(input_data, abs_evidence)
    
    # 6. Confidence & Limitations
    confidence_data, missing_information = ABSConfidenceCalculator.calculate(input_data, abs_evidence)
    
    # Context Assessment Levels (1-5) and Signals
    signals: List[Dict[str, Any]] = []
    level = "LEVEL 1 — NO CLEAR SIGNAL"
    status = "completed"
    
    has_resource_context = "BIOLOGICAL RESOURCE CONTEXT IDENTIFIED" in resource_signals or "NATURAL INGREDIENT CONTEXT IDENTIFIED" in resource_signals
    requires_jurisdiction_review = any("Jurisdiction-Specific Review Recommended" in s for s in jurisdiction_analysis["signals"])
    
    if missing_information and len(missing_information) > 2:
        level = "LEVEL 5 — INSUFFICIENT INFORMATION"
        status = "limited_information"
        signals.append({
            "signal": "INSUFFICIENT INFORMATION FOR CONTEXT ASSESSMENT",
            "priority": "high",
            "explanation": "The system does not have enough information to generate a reliable context signal.",
            "evidence_ids": [],
            "confidence": 0.2
        })
    elif requires_jurisdiction_review:
        level = "LEVEL 4 — JURISDICTION-SPECIFIC REVIEW RECOMMENDED"
        status = "needs_review"
        signals.append({
            "signal": "JURISDICTION-SPECIFIC REVIEW MAY BE REQUIRED",
            "priority": "high",
            "explanation": f"The available context requires more detailed jurisdiction-specific assessment for {input_data.jurisdiction}.",
            "evidence_ids": jurisdiction_analysis["evidence_ids"],
            "confidence": confidence_data.score / 100.0
        })
    elif has_resource_context:
        if "RESOURCE SOURCE INFORMATION LIMITED" in resource_signals or "ORIGIN INFORMATION NOT PROVIDED" in missing_information:
            level = "LEVEL 3 — REVIEW MAY BE APPROPRIATE"
            status = "needs_review"
            signals.append({
                "signal": "ADDITIONAL ABS REVIEW MAY BE APPROPRIATE",
                "priority": "medium",
                "explanation": "Available information indicates a biological-resource context, but source information is incomplete.",
                "evidence_ids": [e.evidence_id for e in abs_evidence],
                "confidence": confidence_data.score / 100.0
            })
            signals.append({
                "signal": "RESOURCE SOURCE INFORMATION IS LIMITED",
                "priority": "medium",
                "explanation": "Resource origin is not provided or incomplete.",
                "evidence_ids": [],
                "confidence": 0.5
            })
        else:
            level = "LEVEL 2 — CONTEXT IDENTIFIED"
            signals.append({
                "signal": "BIOLOGICAL RESOURCE CONTEXT IDENTIFIED",
                "priority": "low",
                "explanation": "Biological resource or utilization context has been identified.",
                "evidence_ids": [],
                "confidence": confidence_data.score / 100.0
            })
    else:
        signals.append({
            "signal": "NO CLEAR ABS SIGNAL FROM AVAILABLE INFORMATION",
            "priority": "low",
            "explanation": "No significant ABS-related signal identified from available information.",
            "evidence_ids": [],
            "confidence": confidence_data.score / 100.0
        })
        
    if "UTILIZATION CONTEXT REQUIRES FURTHER CLARIFICATION" in utilization_analysis["signals"]:
        signals.append({
            "signal": "UTILIZATION CONTEXT REQUIRES CLARIFICATION",
            "priority": "medium",
            "explanation": "The utilization context (e.g., research vs commercial) is unclear.",
            "evidence_ids": [],
            "confidence": 0.5
        })
        
    recommended_actions = []
    if level in ["LEVEL 3 — REVIEW MAY BE APPROPRIATE", "LEVEL 5 — INSUFFICIENT INFORMATION"]:
        recommended_actions.extend(["Clarify the biological resource source.", "Document ingredient origin and sourcing context."])
    if level == "LEVEL 4 — JURISDICTION-SPECIFIC REVIEW RECOMMENDED":
        recommended_actions.extend(["Review relevant jurisdiction-specific information.", "Seek specialist legal or regulatory review where required."])
    if "UTILIZATION CONTEXT REQUIRES CLARIFICATION" in [s["signal"] for s in signals]:
        recommended_actions.append("Clarify research or product development use.")
        
    if not recommended_actions:
        recommended_actions.append("Review the most relevant retrieved evidence.")
        
    return ABSModuleOutput(
        module="abs_context_intelligence",
        status=status,
        summary="Contextual analysis generated based on available resources and jurisdiction. This is not a legal or regulatory determination.",
        context_level=level,
        resource_analysis=ingredient_analysis,
        utilization_context=utilization_analysis,
        jurisdiction_context=jurisdiction_analysis,
        signals=signals,
        supporting_evidence=evidence,
        missing_information=missing_information,
        confidence=confidence_data,
        limitations=confidence_data.limitations,
        recommended_actions=list(set(recommended_actions))
    )
