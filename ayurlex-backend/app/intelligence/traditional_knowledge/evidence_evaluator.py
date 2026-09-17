from typing import List
from app.models.evidence import RetrievedEvidence
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKEvidenceEvaluator:
    @staticmethod
    def evaluate(evidence: List[RetrievedEvidence]) -> List[TKEvidenceContext]:
        """
        Filters evidence to only include valid TK-related metadata.
        """
        evaluated = []
        for item in evidence:
            if item.relevance_score > 0.4:
                evaluated.append(TKEvidenceContext(
                    evidence_id=item.evidence_id,
                    source_title=item.title,
                    category=item.category,
                    language=item.language,
                    source_language="sa", # Mock source language
                    jurisdiction=item.jurisdiction or "India",
                    relevant_excerpt=item.content,
                    relevance_score=item.relevance_score
                ))
        return evaluated
