from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.intelligence.ip.models import IPEvidenceContext
from app.models.intelligence_output import DifferentiationOutput

class DifferentiationAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[IPEvidenceContext]) -> DifferentiationOutput:
        """
        Analyzes how submitted innovation differs from retrieved references.
        """
        signals = []
        evidence_ids = [e.evidence_id for e in evidence]
        
        if evidence:
            # In a real model, this compares specific claims.
            signals.append("Some Differentiating Features Identified")
            signals.append("Further Technical Review Recommended")
        else:
            signals.append("Limited Differentiation Information")
            
        return DifferentiationOutput(
            signals=signals,
            evidence_ids=evidence_ids
        )
