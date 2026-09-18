import os
from typing import List, Dict, Any
import chromadb
from app.rag.models import ChunkMetadata
from app.rag.embeddings.embedding_service import embedding_service

class VectorDatabase:
    """
    Abstract interface for vector database operations using ChromaDB.
    """
    def __init__(self, persist_dir: str = "./chroma_db"):
        self.persist_dir = persist_dir
        self.client = chromadb.PersistentClient(path=self.persist_dir)

    def add_chunks(self, collection_name: str, chunks: List[ChunkMetadata]) -> None:
        if not chunks:
            return
            
        collection = self.client.get_or_create_collection(name=collection_name)
        
        ids = [chunk.chunk_id for chunk in chunks]
        texts = [chunk.content for chunk in chunks]
        # ChromaDB does not allow None values in metadata
        metadatas = []
        for chunk in chunks:
            dump = chunk.model_dump(exclude={"content"})
            clean_meta = {k: v for k, v in dump.items() if v is not None}
            metadatas.append(clean_meta)
        
        # In a production app with large batches, you would want to chunk this insertion
        embeddings = embedding_service.get_embeddings_for_documents(texts)
        
        collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=texts
        )

    def search(self, collection_name: str, query: str, top_k: int = 5, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        try:
            collection = self.client.get_collection(name=collection_name)
        except Exception:
            return []
            
        query_embedding = embedding_service.get_embedding_for_query(query)
        
        # Build ChromaDB where clause from simple dictionary filters
        where_clause = None
        if filters:
            if len(filters) == 1:
                key = list(filters.keys())[0]
                where_clause = {key: filters[key]}
            else:
                where_clause = {"$and": [{k: v} for k, v in filters.items()]}
        
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where_clause
        )
        
        formatted_results = []
        if results and results.get("ids") and len(results["ids"][0]) > 0:
            for i in range(len(results["ids"][0])):
                formatted_results.append({
                    "chunk_id": results["ids"][0][i],
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if results.get("distances") else 0.0
                })
                
        return formatted_results

vector_db = VectorDatabase()
