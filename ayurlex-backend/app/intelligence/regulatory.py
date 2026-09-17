from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.evidence import RetrievedEvidence
from app.models.intelligence_output import ModuleOutput

async def analyze_regulatory(input_data: IntelligenceInput, evidence: List[RetrievedEvidence]) -> ModuleOutput:
    signals = []
    
    if "herbal" in input_data.product_type.lower():
        signals.append("Potential Review Area: Herbal Wellness Product")
    elif "cosmetic" in input_data.product_type.lower():
        signals.append("Potential Review Area: Cosmetic")
    else:
        signals.append("Further Classification Required")
        
    return ModuleOutput(
        module="regulatory_context",
        status="completed",
        signals=signals,
        summary="Regulatory context analysis completed. Findings do not constitute product approval guarantees.",
        evidence_ids=[e.evidence_id for e in evidence],
        confidence=75.0,
        limitations=["Regulatory pathways depend heavily on specific claims made on the product label."],
        recommended_actions=["Consult local regulatory authorities (e.g., AYUSH, FDA) for specific registration pathways."]
    )
