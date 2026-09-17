from typing import List, Set
from app.models.evidence import RetrievedEvidence
from app.intelligence.abs.models import ABSEvidenceContext

class ABSEvidenceEvaluator:
    @staticmethod
    def evaluate(evidence: List[RetrievedEvidence]) -> List[ABSEvidenceContext]:
        """
        Validates, deduplicates, and classifies evidence for ABS context analysis.
        """
        evaluated = []
        seen_ids: Set[str] = set()
        
        # Sort evidence by relevance_score descending to keep the most relevant duplicate
        sorted_evidence = sorted(evidence, key=lambda x: x.relevance_score, reverse=True)
        
        for item in sorted_evidence:
            if item.evidence_id in seen_ids:
                continue
            if item.relevance_score < 0.3:
                continue
                
            seen_ids.add(item.evidence_id)
            
            # Determine ABS Classification Category
            cat_lower = (item.category or "").lower()
            category = item.category or "ABS Context"
            source_type = item.source_type if hasattr(item, 'source_type') else "Document"
            
            evaluated.append(ABSEvidenceContext(
                evidence_id=item.evidence_id,
                source_title=item.title or "Unknown Source",
                source_type=source_type,
                category=category,
                jurisdiction=item.jurisdiction or "International",
                language=item.language or "en",
                relevant_excerpt=item.content,
                relevance_score=item.relevance_score
            ))
            
        return evaluated
