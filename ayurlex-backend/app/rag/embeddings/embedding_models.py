import os
from abc import ABC, abstractmethod
from typing import List

class BaseEmbeddingModel(ABC):
    @abstractmethod
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        pass
        
    @abstractmethod
    def embed_query(self, text: str) -> List[float]:
        pass

class MockEmbeddingModel(BaseEmbeddingModel):
    """
    Mock embedding model for testing and development.
    Returns 384-dimensional zeros.
    """
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [[0.0] * 384 for _ in texts]
        
    def embed_query(self, text: str) -> List[float]:
        return [0.0] * 384

class SentenceTransformerEmbeddingModel(BaseEmbeddingModel):
    """
    Real local embedding model using sentence-transformers.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model_name)
        except ImportError:
            raise ImportError("sentence-transformers is not installed. Please install it to use this model.")
            
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = self.model.encode(texts, show_progress_bar=False)
        return embeddings.tolist()
        
    def embed_query(self, text: str) -> List[float]:
        embedding = self.model.encode(text, show_progress_bar=False)
        return embedding.tolist()
