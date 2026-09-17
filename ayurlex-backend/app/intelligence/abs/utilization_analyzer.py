from typing import Dict, Any, List
from app.models.intelligence_input import IntelligenceInput

class ABSUtilizationAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput) -> Dict[str, Any]:
        """
        Analyzes how the innovation describes the use of ingredients or biological resources.
        Detects Research vs Commercial context.
        """
        signals: List[str] = []
        
        prod_type = (input_data.product_type or "").lower()
        desc = (input_data.innovation_description or "").lower()
        
        if "research" in prod_type or "research" in desc or "study" in desc:
            signals.append("RESEARCH CONTEXT IDENTIFIED")
            
        if "commercial" in prod_type or "market" in desc or "sale" in desc or "product" in prod_type:
            signals.append("COMMERCIALIZATION CONTEXT IDENTIFIED")
            
        if "development" in prod_type or "develop" in desc or "formulat" in desc:
            signals.append("PRODUCT DEVELOPMENT CONTEXT IDENTIFIED")
            
        if not signals:
            signals.append("INSUFFICIENT UTILIZATION INFORMATION")
            signals.append("UTILIZATION CONTEXT REQUIRES FURTHER CLARIFICATION")
            
        return {
            "signals": signals,
            "context_summary": "Utilization context derived from product description and type."
        }
