from typing import List
from app.models.evidence import RetrievedEvidence

class EvidenceRanker:
    """
    Ranks finalized evidence list before returning to intelligence modules.
    """
    def rank(self, evidence: List[RetrievedEvidence]) -> List[RetrievedEvidence]:
        # Sort primarily by relevance score descending
        return sorted(evidence, key=lambda x: x.relevance_score, reverse=True)

evidence_ranker = EvidenceRanker()
