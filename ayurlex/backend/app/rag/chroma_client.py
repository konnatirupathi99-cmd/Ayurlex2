import chromadb
from chromadb.config import Settings
import os

persist_directory = os.path.join(os.path.dirname(__file__), "../../knowledge/chroma")

client = chromadb.PersistentClient(path=persist_directory)

def get_collection(name="ayurlex_knowledge"):
    return client.get_or_create_collection(name=name)
