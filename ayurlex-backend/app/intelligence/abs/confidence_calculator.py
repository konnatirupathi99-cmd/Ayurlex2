from typing import List, Dict, Any, Tuple
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import ConfidenceIndicator
from app.intelligence.abs.models import ABSEvidenceContext

class ABSConfidenceCalculator:
    @staticmethod
    def calculate(input_data: IntelligenceInput, evidence: List[ABSEvidenceContext]) -> Tuple[ConfidenceIndicator, List[str]]:
        """
        Calculates confidence for ABS Context Intelligence.
        Returns the ConfidenceIndicator and a list of explicit missing_information strings.
        """
        score = 0.0
        limitations = []
        missing_information = []
        
        # Input completeness
        if input_data.ingredients:
            score += 20
        else:
            limitations.append("Missing ingredients.")
            missing_information.append("INGREDIENT IDENTIFICATION AMBIGUOUS")
            
        if input_data.resource_source_information:
            score += 20
        else:
            limitations.append("Resource origin not available.")
            missing_information.append("RESOURCE ORIGIN NOT PROVIDED")
            missing_information.append("SOURCE INFORMATION NOT PROVIDED")
            
        if not input_data.jurisdiction or input_data.jurisdiction.lower() == "other / not specified":
            limitations.append("Jurisdiction not specified.")
            missing_information.append("JURISDICTION NOT SPECIFIED")
        else:
            score += 20
            
        # Utilization context
        if not input_data.product_type and not input_data.innovation_description:
            limitations.append("Utilization context unclear.")
            missing_information.append("UTILIZATION CONTEXT UNCLEAR")
            missing_information.append("PRODUCT DEVELOPMENT CONTEXT INCOMPLETE")
        else:
            score += 20
            
        # Evidence Availability
        if evidence:
            score += 20
            if any(e.relevance_score > 0.8 for e in evidence):
                pass
            else:
                limitations.append("Limited ABS-related evidence relevance.")
        else:
            limitations.append("Limited ABS-related evidence coverage.")
            
        level = "high" if score >= 80 else "moderate" if score >= 50 else "low"
        
        conf = ConfidenceIndicator(
            score=min(100.0, score),
            level=level,
            explanation="Confidence represents confidence in the system's contextual analysis based on available information. It does not represent legal certainty or compliance status.",
            limitations=limitations
        )
        
        return conf, missing_information
