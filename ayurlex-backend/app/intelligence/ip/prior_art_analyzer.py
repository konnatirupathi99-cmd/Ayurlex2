from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.intelligence.ip.models import IPEvidenceContext
from app.models.intelligence_output import PriorArtOutput

class PriorArtAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[IPEvidenceContext]) -> PriorArtOutput:
        """
        Analyzes retrieved evidence for prior-art signals.
        """
        signals = []
        evidence_ids = [e.evidence_id for e in evidence]
        
        if not evidence:
            status = "Limited Relevant Evidence Retrieved"
            signals.append("Further Prior-Art Review Recommended")
        else:
            status = "Relevant Prior-Art Evidence Retrieved"
            signals.append("Potential Similarity Identified")
            
        return PriorArtOutput(
            status=status,
            similarity_signals=signals,
            evidence_ids=evidence_ids
        )
