from typing import List, Dict, Any
from app.rag.models import ChunkMetadata

class KeywordIndexManager:
    """
    Handles keyword indexing using BM25.
    """
    def __init__(self):
        self._store: Dict[str, List[ChunkMetadata]] = {}
        self._bm25_indices: Dict[str, Any] = {}
        
    def _tokenize(self, text: str) -> List[str]:
        return text.lower().split()
        
    def add_chunks(self, collection_name: str, chunks: List[ChunkMetadata]):
        if collection_name not in self._store:
            self._store[collection_name] = []
        self._store[collection_name].extend(chunks)
        
        # Rebuild BM25 index for the collection
        try:
            from rank_bm25 import BM25Okapi
            tokenized_corpus = [self._tokenize(chunk.content) for chunk in self._store[collection_name]]
            if tokenized_corpus:
                self._bm25_indices[collection_name] = BM25Okapi(tokenized_corpus)
        except ImportError:
            pass
        
    def search(self, collection_name: str, query: str, top_k: int = 5, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        if collection_name not in self._store or not self._store[collection_name]:
            return []
            
        chunks = self._store[collection_name]
        tokenized_query = self._tokenize(query)
        
        # Determine if we have BM25 available
        if collection_name in self._bm25_indices:
            bm25 = self._bm25_indices[collection_name]
            doc_scores = bm25.get_scores(tokenized_query)
        else:
            # Fallback simple scoring
            doc_scores = []
            query_terms = set(tokenized_query)
            for chunk in chunks:
                chunk_lower = chunk.content.lower()
                score = sum(1 for term in query_terms if term in chunk_lower)
                doc_scores.append(score)
                
        results = []
        for idx, chunk in enumerate(chunks):
            # Apply filters
            if filters:
                match = True
                for k, v in filters.items():
                    if getattr(chunk, k, None) != v:
                        match = False
                        break
                if not match:
                    continue
                    
            score = doc_scores[idx]
            if score > 0:
                results.append({
                    "chunk_id": chunk.chunk_id,
                    "content": chunk.content,
                    "metadata": chunk.model_dump(exclude={"content"}),
                    "score": score
                })
                
        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

keyword_index = KeywordIndexManager()
