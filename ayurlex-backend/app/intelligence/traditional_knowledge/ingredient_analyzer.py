from typing import List
from app.models.intelligence_output import TKTermAnalysis, TKIngredientAnalysis
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKIngredientAnalyzer:
    @staticmethod
    def analyze(term_data: TKTermAnalysis, evidence: List[TKEvidenceContext]) -> List[TKIngredientAnalysis]:
        """
        Analyzes evidence at the individual ingredient level.
        Matches each normalized ingredient to retrieved evidence.
        """
        results = []
        
        for term in term_data.normalized_terms:
            term_lower = term.lower()
            matched_evidence = []
            
            for e in evidence:
                if term_lower in e.relevant_excerpt.lower() or term_lower in e.source_title.lower():
                    matched_evidence.append(e)
            
            if matched_evidence:
                results.append(TKIngredientAnalysis(
                    ingredient=term,
                    traditional_context="Potentially relevant traditional references were retrieved for this ingredient.",
                    evidence_ids=[e.evidence_id for e in matched_evidence],
                    confidence=min(1.0, 0.5 + (len(matched_evidence) * 0.15))
                ))
            else:
                results.append(TKIngredientAnalysis(
                    ingredient=term,
                    traditional_context="No direct traditional references retrieved specifically for this ingredient.",
                    evidence_ids=[],
                    confidence=0.2
                ))
                
        return results
