from typing import List, Dict, Any
from app.models.intelligence_input import IntelligenceInput
from app.intelligence.formulation.models import FormulationEvidenceContext

class FormulationConfidenceCalculator:
    @staticmethod
    def calculate(input_data: IntelligenceInput, similarity_score: float, evidence: List[FormulationEvidenceContext]) -> Dict[str, Any]:
        """
        Calculates a confidence score specifically for Formulation classification.
        """
        score = 0.0
        limitations = []
        
        # 1. Input Completeness (0-40)
        if input_data.ingredients:
            score += 20
        else:
            limitations.append("Ingredient information is incomplete.")
            
        if input_data.product_type:
            score += 20
        else:
            limitations.append("Product type/intended purpose is unspecified.")
            
        # 2. Similarity Reliability (0-30)
        score += (similarity_score * 30)
        
        # 3. Evidence Support (0-30)
        if evidence:
            score += min(len(evidence) * 10, 30)
        else:
            limitations.append("Knowledge retrieval coverage may be incomplete.")
            limitations.append("Absence of retrieved evidence does not establish novelty.")
            
        score = round(min(score, 100), 1)
        
        level = "high" if score >= 75 else "moderate" if score >= 40 else "low"
        
        return {
            "score": score,
            "level": level,
            "explanation": "Confidence is based on input completeness, similarity to known patterns, and retrieved evidence.",
            "limitations": limitations
        }
