import os
from typing import List
from app.rag.embeddings.embedding_models import BaseEmbeddingModel, MockEmbeddingModel, SentenceTransformerEmbeddingModel

class EmbeddingService:
    def __init__(self):
        # Allow environment configuration for embedding models
        model_type = os.getenv("EMBEDDING_MODEL_TYPE", "mock").lower()
        if model_type == "sentence_transformer":
            self.model: BaseEmbeddingModel = SentenceTransformerEmbeddingModel()
        else:
            self.model: BaseEmbeddingModel = MockEmbeddingModel()
            
    def get_embeddings_for_documents(self, texts: List[str]) -> List[List[float]]:
        return self.model.embed_documents(texts)
        
    def get_embedding_for_query(self, text: str) -> List[float]:
        return self.model.embed_query(text)

embedding_service = EmbeddingService()
