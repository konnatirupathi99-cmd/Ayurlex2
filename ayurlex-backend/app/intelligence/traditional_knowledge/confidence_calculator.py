from typing import List, Dict, Any
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import ConfidenceIndicator
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKConfidenceCalculator:
    @staticmethod
    def calculate(input_data: IntelligenceInput, evidence: List[TKEvidenceContext]) -> ConfidenceIndicator:
        """
        Calculates confidence for TK based on available information and evidence.
        """
        score = 0.0
        limitations = []
        
        # 1. Input completeness
        if input_data.ingredients:
            score += 20
        else:
            limitations.append("Missing ingredients.")
            
        if not input_data.formulation_context:
            limitations.append("The formulation method was not provided.")
            
        # 2. Term normalization quality
        if input_data.normalized_ingredients:
            if len(input_data.normalized_ingredients) == len(input_data.ingredients) and len(input_data.ingredients) > 0:
                score += 20
            else:
                score += 10
                limitations.append("Ambiguous terminology: some terms could not be perfectly mapped.")
        else:
            limitations.append("Ambiguous terminology: normalization failed.")
            
        # 3. Evidence availability and relevance
        if evidence:
            score += 30
            # Check for high relevance
            if any(e.relevance_score > 0.8 for e in evidence):
                score += 30
            else:
                score += 10
                limitations.append("Weak evidence relevance.")
        else:
            limitations.append("Limited traditional knowledge evidence.")
            limitations.append("Available evidence may not represent complete traditional knowledge coverage.")
            
        level = "high" if score >= 80 else "moderate" if score >= 50 else "low"
        
        return ConfidenceIndicator(
            score=min(100.0, score),
            level=level,
            explanation="Confidence represents confidence in the available evidence analysis, not legal certainty regarding traditional knowledge status.",
            limitations=limitations
        )
