from typing import List, Dict, Any
from app.models.intelligence_output import ConfidenceIndicator

class ConfidenceCalculator:
    def calculate(self, missing_info: List[str], evidence_count: int, signals: List[str]) -> ConfidenceIndicator:
        base_score = 0.8
        limitations = []
        
        if len(missing_info) > 0:
            penalty = min(0.3, len(missing_info) * 0.1)
            base_score -= penalty
            limitations.append(f"Missing {len(missing_info)} key pieces of information.")
            
        if evidence_count == 0:
            base_score -= 0.2
            limitations.append("LIMITED REGULATORY EVIDENCE")
            
        if "MULTIPLE PRODUCT CONTEXTS POSSIBLE" in signals:
            base_score -= 0.1
            limitations.append("PRODUCT CLASSIFICATION AMBIGUOUS")
            
        final_score = max(0.1, min(1.0, base_score))
        
        if final_score >= 0.7:
            level = "high"
        elif final_score >= 0.4:
            level = "moderate"
        else:
            level = "low"
            
        return ConfidenceIndicator(
            score=final_score,
            level=level,
            explanation="Confidence represents confidence in the available contextual analysis. It does not represent regulatory approval, legal compliance, or legal certainty.",
            limitations=limitations
        )
