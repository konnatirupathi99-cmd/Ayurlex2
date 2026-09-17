from typing import List
from app.models.evidence import RetrievedEvidence
from app.intelligence.formulation.models import FormulationEvidenceContext

class EvidenceEvaluator:
    @staticmethod
    def evaluate(evidence: List[RetrievedEvidence]) -> List[FormulationEvidenceContext]:
        """
        Validates and parses evidence specifically for formulation context.
        Returns a structured list of formulation evidence contexts.
        """
        evaluated = []
        for item in evidence:
            if item.relevance_score > 0.3: # Minimum threshold
                evaluated.append(FormulationEvidenceContext(
                    evidence_id=item.evidence_id,
                    source_title=item.title,
                    category=item.category,
                    language=item.language,
                    relevant_excerpt=item.content,
                    relevance_score=item.relevance_score
                ))
        return evaluated
