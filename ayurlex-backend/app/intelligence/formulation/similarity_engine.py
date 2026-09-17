from typing import List, Dict, Any
from app.models.responses import NormalizedTerm
from app.intelligence.formulation.models import FormulationEvidenceContext

class SimilarityEngine:
    @staticmethod
    def calculate_similarity(ingredients: List[NormalizedTerm], evidence: List[FormulationEvidenceContext]) -> Dict[str, Any]:
        """
        Mock Similarity Engine.
        In production, compares normalized ingredients against classical formulation vectors.
        """
        canonical_ingredients = [i.normalized.lower() for i in ingredients]
        
        # Mock Logic for Prototype Classification
        # We simulate the vector DB similarity score based on combinations
        
        if not canonical_ingredients:
            return {"pattern": "missing", "score": 0.0}
            
        if "ashwagandha" in canonical_ingredients and "tulsi" in canonical_ingredients:
            return {"pattern": "proprietary", "score": 0.7} # Mixed/custom pattern
            
        if "ashwagandha" in canonical_ingredients and "turmeric" in canonical_ingredients:
            return {"pattern": "classical", "score": 0.9} # High match to mock classical text
            
        if canonical_ingredients:
            return {"pattern": "novel", "score": 0.1} # No overlap with known classical patterns
            
        return {"pattern": "unclear", "score": 0.0}
