from app.rag.vector_store import vector_store

def retrieve_evidence(query: str, language: str = "en"):
    """
    Retrieve semantic context from the vector store using multilingual embeddings.
    """
    results = vector_store.search(query, language=language)
    return results
