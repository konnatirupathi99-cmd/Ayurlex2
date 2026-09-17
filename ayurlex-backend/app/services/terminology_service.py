import json
import os
from typing import List
from app.models.responses import NormalizedTerm

TERMINOLOGY_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'terminology.json')

def load_terminology():
    if os.path.exists(TERMINOLOGY_PATH):
        with open(TERMINOLOGY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def normalize_terms(ingredients: List[str]) -> List[NormalizedTerm]:
    """
    Maps multilingual ingredient names to their canonical/scientific names.
    """
    db = load_terminology()
    results = []
    
    for item in ingredients:
        normalized = None
        # Simple lookup
        for key, value in db.items():
            if item.lower() in [alias.lower() for alias in value.get("aliases", [])] or item.lower() == key.lower():
                normalized = NormalizedTerm(
                    user_input=item,
                    normalized=value.get("canonical", key),
                    scientific=value.get("scientific", ""),
                    english=value.get("english", "")
                )
                break
                
        if not normalized:
            # Fallback if not found
            normalized = NormalizedTerm(user_input=item, normalized=item)
            
        results.append(normalized)
        
    return results
