import uuid
from typing import List, Dict, Any, Tuple
from app.models.evidence import RetrievedEvidence

class EvidenceValidator:
    """
    Validates retrieved chunks before sending them to the Intelligence Engine.
    """
    def validate_and_convert(self, results: List[Dict[str, Any]], target_jurisdiction: str) -> Tuple[List[RetrievedEvidence], List[str]]:
        valid_evidence = []
        limitations = []
        
        seen_chunks = set()
        seen_content_hashes = set()
        
        for res in results:
            chunk_id = res.get("chunk_id")
            if not chunk_id or chunk_id in seen_chunks:
                continue
                
            seen_chunks.add(chunk_id)
            
            content = res.get("content", "").strip()
            if not content:
                continue
                
            content_hash = hash(content)
            if content_hash in seen_content_hashes:
                continue
                
            seen_content_hashes.add(content_hash)
            
            meta = res.get("metadata", {})
            jurisdiction = meta.get("jurisdiction", "International")
            
            # Warn if we included a mismatch (though reranker should have handled it)
            if jurisdiction != "International" and target_jurisdiction != "International" and jurisdiction != target_jurisdiction:
                limitations.append(f"Included evidence from {jurisdiction} which may not apply to target {target_jurisdiction}.")
                
            evidence = RetrievedEvidence(
                evidence_id=f"EV-{uuid.uuid4().hex[:8]}",
                document_id=meta.get("document_id", "unknown"),
                chunk_id=chunk_id,
                source_title=meta.get("title", "Unknown Source"),
                source_name=meta.get("source"),
                source_type=meta.get("category", "General"), # changed source_type to map to category or something since source_type was removed
                category=meta.get("category", "General"),
                jurisdiction=jurisdiction,
                jurisdiction_scope=meta.get("authority"), # mapped jurisdiction_scope to authority for backward compatibility
                language=meta.get("language", "en"),
                section=meta.get("section"),
                page_number=meta.get("page"), # might need conversion to int if it expects int, but model says Optional[int]. We can just pass the string if we change the model.
                content=content,
                original_content=content,
                relevance_score=float(res.get("relevance_score", 0.0)),
                match_type="SEMANTIC_MATCH" if "distance" in res else "KEYWORD_MATCH",
                retrieval_method="hybrid"
            )
            
            valid_evidence.append(evidence)
            
        if not valid_evidence:
            limitations.append("NO RETRIEVED RESULT DOES NOT MEAN NO INFORMATION EXISTS.")
            
        return valid_evidence, limitations

evidence_validator = EvidenceValidator()
