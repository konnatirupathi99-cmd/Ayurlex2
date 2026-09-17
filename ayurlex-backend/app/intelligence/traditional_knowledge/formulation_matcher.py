from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import TKFormulationAnalysis
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKFormulationMatcher:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[TKEvidenceContext]) -> TKFormulationAnalysis:
        """
        Analyzes formulation-level similarity as opposed to ingredient-level similarity.
        """
        signals = []
        evidence_ids = [e.evidence_id for e in evidence]
        
        if evidence:
            signals.append("Partial formulation-level similarity requires further review")
            signals.append("Related Traditional Preparation Context")
        else:
            signals.append("Limited Formulation-Level Evidence")
            signals.append("No Clear Close Match Retrieved")
            
        return TKFormulationAnalysis(
            signals=signals,
            evidence_ids=evidence_ids
        )
