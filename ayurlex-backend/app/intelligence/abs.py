from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.evidence import RetrievedEvidence
from app.models.intelligence_output import ModuleOutput

async def analyze_abs(input_data: IntelligenceInput, evidence: List[RetrievedEvidence]) -> ModuleOutput:
    signals = []
    
    # Mock ABS logic
    if input_data.jurisdiction.lower() == "india":
        signals.append("Additional Review May Be Appropriate")
        signals.append("Jurisdiction-Specific Review Recommended")
        status = "needs_review"
    else:
        signals.append("No Clear Signal From Available Information")
        status = "completed"
        
    return ModuleOutput(
        module="abs_context",
        status=status,
        signals=signals,
        summary="Biological resource and ABS context analysis generated based on jurisdiction.",
        evidence_ids=[e.evidence_id for e in evidence],
        confidence=70.0,
        limitations=["SYSTEM INTELLIGENCE SIGNAL: This is not a legal or regulatory determination of ABS compliance."],
        recommended_actions=["Verify requirements under local biodiversity laws (e.g., National Biodiversity Authority in India)."]
    )
