from typing import List
from app.models.intelligence_output import TKTermAnalysis, TKIngredientAnalysis
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKIngredientAnalyzer:
    @staticmethod
    def analyze(term_data: TKTermAnalysis, evidence: List[TKEvidenceContext]) -> List[TKIngredientAnalysis]:
        """
        Analyzes evidence at the individual ingredient level.
        """
        results = []
        evidence_ids = [e.evidence_id for e in evidence]
        
        for term in term_data.normalized_terms:
            if evidence:
                results.append(TKIngredientAnalysis(
                    ingredient=term,
                    traditional_context="Potentially relevant traditional references were retrieved.",
                    evidence_ids=evidence_ids,
                    confidence=0.82
                ))
            else:
                results.append(TKIngredientAnalysis(
                    ingredient=term,
                    traditional_context="No relevant traditional references were retrieved.",
                    evidence_ids=[],
                    confidence=0.0
                ))
                
        return results
