from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import TKUseAnalysis
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKUseContextAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[TKEvidenceContext]) -> TKUseAnalysis:
        """
        Analyzes the intended use context against classical use contexts.
        """
        signals = []
        evidence_ids = [e.evidence_id for e in evidence]
        
        if evidence:
            signals.append("Related use context was identified in available evidence")
            signals.append("Potentially Related Traditional Use Identified")
        else:
            signals.append("Limited Use-Level Evidence")
            
        return TKUseAnalysis(
            signals=signals,
            evidence_ids=evidence_ids
        )
