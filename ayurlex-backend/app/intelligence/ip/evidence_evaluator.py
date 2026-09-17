from typing import List
from app.models.evidence import RetrievedEvidence
from app.intelligence.ip.models import IPEvidenceContext

class IPEvidenceEvaluator:
    @staticmethod
    def evaluate(evidence: List[RetrievedEvidence], jurisdiction: str) -> List[IPEvidenceContext]:
        """
        Filters evidence to only include valid IP-related metadata and separates by jurisdiction.
        """
        evaluated = []
        for item in evidence:
            # For IP, we want a higher relevance threshold to avoid hallucinating patents
            if item.relevance_score > 0.4:
                # Add strict check in production to ensure source is IP-related (e.g. patent DB)
                evaluated.append(IPEvidenceContext(
                    evidence_id=item.evidence_id,
                    source_title=item.title,
                    category=item.category,
                    language=item.language,
                    jurisdiction=item.jurisdiction or jurisdiction,
                    relevant_excerpt=item.content,
                    relevance_score=item.relevance_score
                ))
        return evaluated
