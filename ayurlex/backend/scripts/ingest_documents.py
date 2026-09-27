import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.rag.chroma_client import get_collection

def ingest_seed_data():
    collection = get_collection()
    
    # Mock documents for the prototype
    documents = [
        "Ashwagandha (Withania somnifera) is used in Ayurveda for stress relief and vitality. It is traditionally considered a Medhya Rasayana (rejuvenator).",
        "Under Section 3(p) of the Indian Patents Act, 1970, an invention which in effect is traditional knowledge or which is an aggregation or duplication of known properties of traditionally known component or components is not patentable.",
        "The Traditional Knowledge Digital Library (TKDL) contains documentation of Ayurvedic formulations to prevent bio-piracy.",
        "Turmeric (Curcuma longa) is widely used for its anti-inflammatory properties. A famous patent on the use of Turmeric for wound healing (US Patent 5,401,504) was revoked after India successfully proved it was prior art based on traditional Ayurvedic knowledge.",
        "Regulatory approval for Ayurvedic proprietary medicines in India requires compliance with the Drugs and Cosmetics Act, 1940, and Rules, 1945."
    ]
    
    metadatas = [
        {"source": "Ayurvedic Pharmacopoeia", "jurisdiction": "India", "category": "AYURVEDA", "terminology": "Ashwagandha, Withania somnifera"},
        {"source": "Indian Patents Act, 1970", "jurisdiction": "India", "category": "INTELLECTUAL_PROPERTY", "terminology": "Patentability"},
        {"source": "TKDL Information", "jurisdiction": "International", "category": "TRADITIONAL_KNOWLEDGE", "terminology": ""},
        {"source": "CSIR TKDL Case Study", "jurisdiction": "United States, India", "category": "IP_PATENT", "terminology": "Turmeric, Curcuma longa"},
        {"source": "Drugs and Cosmetics Act, 1940", "jurisdiction": "India", "category": "REGULATORY", "terminology": "Proprietary Medicine"}
    ]
    
    ids = [f"doc_{i}" for i in range(len(documents))]
    
    print("Ingesting data into ChromaDB...")
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print("Ingestion complete!")

if __name__ == "__main__":
    ingest_seed_data()
