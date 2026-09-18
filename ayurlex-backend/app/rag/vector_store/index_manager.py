from typing import List, Dict, Any
from app.rag.models import ChunkMetadata

class KeywordIndexManager:
    """
    Handles keyword indexing alongside vectors.
    In a real system, this would back to ElasticSearch or similar.
    For this implementation, we use an in-memory exact match / BM25 approach 
    that operates on the returned documents from Chroma, or a parallel local store.
    """
    def __init__(self):
        self._store: Dict[str, List[ChunkMetadata]] = {}
        
    def add_chunks(self, collection_name: str, chunks: List[ChunkMetadata]):
        if collection_name not in self._store:
            self._store[collection_name] = []
        self._store[collection_name].extend(chunks)
        
    def search(self, collection_name: str, query: str, top_k: int = 5, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        # Extremely basic exact keyword match as fallback
        if collection_name not in self._store:
            return []
            
        results = []
        query_terms = set(query.lower().split())
        
        for chunk in self._store[collection_name]:
            # Apply filters
            if filters:
                match = True
                for k, v in filters.items():
                    if getattr(chunk, k, None) != v:
                        match = False
                        break
                if not match:
                    continue
            
            chunk_lower = chunk.content.lower()
            # Score based on how many terms from the query are in the chunk
            score = sum(1 for term in query_terms if term in chunk_lower)
            if score > 0:
                results.append({
                    "chunk_id": chunk.chunk_id,
                    "content": chunk.content,
                    "metadata": chunk.model_dump(exclude={"content"}),
                    "score": score / len(query_terms)  # Normalize
                })
                
        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

keyword_index = KeywordIndexManager()
