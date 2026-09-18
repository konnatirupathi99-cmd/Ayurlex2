from typing import List, Dict, Any
from app.rag.vector_store.vector_database import vector_db

class VectorSearchEngine:
    def search(self, collections: List[str], query: str, filters: Dict[str, Any], top_k: int = 5) -> List[Dict[str, Any]]:
        results = []
        for coll in collections:
            coll_results = vector_db.search(coll, query, top_k=top_k, filters=filters)
            results.extend(coll_results)
            
        # Sort combined results by distance (lower is better for Chroma)
        results.sort(key=lambda x: x.get("distance", 1.0))
        return results[:top_k]

vector_search = VectorSearchEngine()
