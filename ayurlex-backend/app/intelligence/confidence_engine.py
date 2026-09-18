from typing import Dict, List
from app.models.intelligence_output import ModuleOutput, ConfidenceIndicator

class ConfidenceEngine:
    @staticmethod
    def calculate(modules: Dict[str, ModuleOutput], evidence_count: int, input_completeness: float) -> ConfidenceIndicator:
        """
        Calculates a transparent confidence score based on evidence, completeness, and module status.
        """
        score = 0.0
        
        # 1. Evidence Quality/Quantity (up to 40 points)
        evidence_score = min(evidence_count * 10, 40)
        score += evidence_score
        
        # 2. Input Completeness (up to 30 points)
        score += (input_completeness * 30)
        
        # 3. Module Confidence Aggregation (up to 30 points)
        mod_confidences = []
        for mod in modules.values():
            if mod.status != "failed":
                if hasattr(mod.confidence, 'score'):
                    # The score could be normalized to 0-1 or 0-100, assuming 0-100 based on old usage, but ConfidenceIndicator might use 0-1.
                    val = mod.confidence.score
                    if val <= 1.0: val *= 100
                    mod_confidences.append(val)
                else:
                    mod_confidences.append(float(mod.confidence))
                    
        avg_mod_conf = sum(mod_confidences) / len(mod_confidences) if mod_confidences else 0
        score += (avg_mod_conf * 0.3)
        
        score = round(min(score, 100), 1)
        
        # Determine Level
        level = "High" if score >= 75 else "Moderate" if score >= 40 else "Low"
        
        limitations = []
        if score < 50:
            limitations.append("Confidence is low due to limited evidence or missing input data.")
            
        return ConfidenceIndicator(
            score=score,
            level=level,
            explanation="Confidence is based on available evidence, input completeness, and module consistency.",
            limitations=limitations
        )
