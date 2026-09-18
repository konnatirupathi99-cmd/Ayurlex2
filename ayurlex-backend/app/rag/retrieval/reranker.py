from typing import List, Dict, Any

class Reranker:
    """
    After retrieval, re-rank evidence based on relevance, jurisdiction match, etc.
    """
    def rerank(self, results: List[Dict[str, Any]], query_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        # In a more advanced implementation, this could use a cross-encoder (e.g., MS MARCO MiniLM)
        # For now, we adjust scores based on jurisdiction and category heuristics
        target_jurisdiction = query_analysis.get("jurisdiction", "International")
        
        for res in results:
            meta = res.get("metadata", {})
            score = res.get("relevance_score", 0.0)
            
            # Boost score if jurisdiction matches exactly
            if meta.get("jurisdiction") == target_jurisdiction:
                score *= 1.2
            
            # Penalize slightly if it's completely missing
            if not meta.get("jurisdiction"):
                score *= 0.9
                
            res["relevance_score"] = score
            
        # Re-sort
        results.sort(key=lambda x: x.get("relevance_score", 0.0), reverse=True)
        return results

reranker = Reranker()
