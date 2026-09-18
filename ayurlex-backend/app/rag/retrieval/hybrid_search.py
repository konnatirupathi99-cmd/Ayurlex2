from typing import List, Dict, Any
from app.rag.retrieval.vector_search import vector_search
from app.rag.retrieval.keyword_search import keyword_search

class HybridSearchEngine:
    def search(self, collections: List[str], query: str, filters: Dict[str, Any], top_k: int = 10) -> List[Dict[str, Any]]:
        # Fetch results from both engines
        vec_results = vector_search.search(collections, query, filters, top_k=top_k)
        kw_results = keyword_search.search(collections, query, filters, top_k=top_k)
        
        # Simple reciprocal rank fusion (RRF)
        scores = {}
        combined_results = {}
        
        def apply_rrf(results, rank_constant=60):
            for rank, res in enumerate(results):
                chunk_id = res["chunk_id"]
                if chunk_id not in scores:
                    scores[chunk_id] = 0.0
                    combined_results[chunk_id] = res
                scores[chunk_id] += 1.0 / (rank_constant + rank + 1)

        apply_rrf(vec_results)
        apply_rrf(kw_results)
        
        # Sort by RRF score
        sorted_chunks = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        final_results = []
        for chunk_id, score in sorted_chunks[:top_k]:
            res = combined_results[chunk_id]
            res["relevance_score"] = score
            final_results.append(res)
            
        return final_results

hybrid_search = HybridSearchEngine()
