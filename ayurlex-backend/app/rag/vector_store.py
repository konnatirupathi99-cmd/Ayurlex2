import os

class ChromaStoreMock:
    def __init__(self):
        self.persist_directory = os.getenv("CHROMA_DB_PATH", "./chroma_db")
        
    def add_documents(self, documents):
        pass
        
    def search(self, query, language="en", limit=5):
        # Mock retrieval
        return []

vector_store = ChromaStoreMock()
