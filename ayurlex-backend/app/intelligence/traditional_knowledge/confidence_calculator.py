from typing import List, Dict, Any
from app.models.intelligence_input import IntelligenceInput
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKConfidenceCalculator:
    @staticmethod
    def calculate(input_data: IntelligenceInput, evidence: List[TKEvidenceContext]) -> Dict[str, Any]:
        """
        Calculates confidence for TK based on available information and evidence.
        """
        score = 0.0
        limitations = []
        
        if input_data.ingredients:
            score += 20
        else:
            limitations.append("Missing ingredients.")
            
        if input_data.normalized_ingredients:
            score += 20
        else:
            limitations.append("Ambiguous terminology: normalization failed.")
            
        if evidence:
            score += 60
        else:
            limitations.append("Limited traditional knowledge evidence.")
            limitations.append("Available evidence may not represent complete traditional knowledge coverage.")
            
        level = "high" if score >= 80 else "moderate" if score >= 40 else "low"
        
        return {
            "score": score,
            "level": level,
            "explanation": "Confidence represents confidence in the available evidence analysis, not legal certainty regarding traditional knowledge status.",
            "limitations": limitations
        }
