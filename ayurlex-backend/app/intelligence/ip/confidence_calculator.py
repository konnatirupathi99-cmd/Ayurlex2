from typing import List, Dict, Any
from app.models.intelligence_input import IntelligenceInput
from app.intelligence.ip.models import IPEvidenceContext

class IPConfidenceCalculator:
    @staticmethod
    def calculate(input_data: IntelligenceInput, evidence: List[IPEvidenceContext]) -> Dict[str, Any]:
        """
        Calculates confidence for IP specifically. 
        It explicitly penalizes lack of evidence to prevent legal hallucinations.
        """
        score = 0.0
        limitations = []
        
        if input_data.ingredients:
            score += 20
        else:
            limitations.append("Incomplete innovation description: missing ingredients.")
            
        if input_data.innovation_description:
            score += 20
        else:
            limitations.append("Missing technical details.")
            
        if evidence:
            score += 40
        else:
            limitations.append("Limited evidence retrieved.")
            limitations.append("Available evidence retrieval may not represent a complete prior-art search.")
            
        if not input_data.jurisdiction:
            limitations.append("Missing jurisdiction information.")
        else:
            score += 20
            
        level = "high" if score >= 80 else "moderate" if score >= 40 else "low"
        
        return {
            "score": score,
            "level": level,
            "explanation": "Confidence represents analysis confidence based on available information. It does not represent legal certainty or patentability.",
            "limitations": limitations
        }
