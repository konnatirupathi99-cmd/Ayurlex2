from typing import List, Set
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import TKUseAnalysis
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKUseContextAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[TKEvidenceContext]) -> TKUseAnalysis:
        """
        Analyzes the intended use context against classical use contexts.
        """
        signals: Set[str] = set()
        matched_evidence_ids: Set[str] = set()
        
        # Simple extraction of keywords from description to match use cases
        # In a real scenario, this would use NLP to extract specific therapeutic uses
        use_keywords = [w.lower() for w in input_data.innovation_description.split() if len(w) > 4]
        
        for e in evidence:
            text = e.relevant_excerpt.lower()
            matches = sum(1 for kw in use_keywords if kw in text)
            
            if matches > 0:
                matched_evidence_ids.add(e.evidence_id)
                if matches >= max(1, len(use_keywords) // 4):
                    signals.add("Potentially Related Traditional Use Identified")
                    signals.add("Related Traditional Context Found")
                else:
                    signals.add("Partial Use-Level Similarity")
                    
        if not matched_evidence_ids:
            signals.add("Limited Use-Level Evidence")
            if evidence:
                signals.add("Further Specialist Review Recommended")
            
        return TKUseAnalysis(
            signals=list(signals),
            evidence_ids=list(matched_evidence_ids)
        )
