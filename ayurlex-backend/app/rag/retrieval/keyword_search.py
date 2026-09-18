from typing import List, Dict, Any
from app.rag.vector_store.index_manager import keyword_index

class KeywordSearchEngine:
    def search(self, collections: List[str], query: str, filters: Dict[str, Any], top_k: int = 5) -> List[Dict[str, Any]]:
        results = []
        for coll in collections:
            coll_results = keyword_index.search(coll, query, top_k=top_k, filters=filters)
            results.extend(coll_results)
            
        # Sort combined results by score (higher is better for keywords)
        results.sort(key=lambda x: x.get("score", 0.0), reverse=True)
        return results[:top_k]

keyword_search = KeywordSearchEngine()
