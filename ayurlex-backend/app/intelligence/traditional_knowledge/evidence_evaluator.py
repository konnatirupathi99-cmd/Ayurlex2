from typing import List, Set
from app.models.evidence import RetrievedEvidence
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKEvidenceEvaluator:
    @staticmethod
    def evaluate(evidence: List[RetrievedEvidence]) -> List[TKEvidenceContext]:
        """
        Validates, deduplicates, and classifies evidence for TK analysis.
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
            
            # Determine TK Classification Category
            cat_lower = (item.category or "").lower()
            category = item.category
            source_type = "Traditional Reference"
            
            if "classical" in cat_lower or "samhita" in cat_lower:
                category = "Classical Ayurvedic Reference"
                source_type = "Classical Text"
            elif "tkdl" in cat_lower or "traditional" in cat_lower:
                category = "Traditional Knowledge Reference"
                source_type = "TK Database"
            elif "ingredient" in cat_lower:
                category = "Ingredient Reference"
                source_type = "Pharmacopeia"
            else:
                if not category:
                    category = "Contextual Evidence"
            
            evaluated.append(TKEvidenceContext(
                evidence_id=item.evidence_id,
                source_title=item.title or "Unknown Source",
                source_type=source_type,
                category=category,
                language=item.language or "en",
                source_language=getattr(item, "source_language", "sa"),
                jurisdiction=item.jurisdiction or "India",
                relevant_excerpt=item.content,
                relevance_score=item.relevance_score
            ))
            
        return evaluated
