from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import ABSResourceAnalysis, ConfidenceIndicator
from app.intelligence.abs.models import ABSEvidenceContext

class ABSIngredientContextAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[ABSEvidenceContext]) -> List[ABSResourceAnalysis]:
        """
        Analyzes each ingredient independently against available resource context.
        """
        results = []
        
        for term in input_data.normalized_ingredients:
            term_name = term.normalized or term.user_input
            matched_evidence = []
            signals = []
            
            # Simple keyword matching for evidence
            for e in evidence:
                if term_name.lower() in e.relevant_excerpt.lower() or term_name.lower() in e.source_title.lower():
                    matched_evidence.append(e)
            
            if matched_evidence:
                signals.append("RESOURCE CONTEXT AVAILABLE")
            else:
                signals.append("INSUFFICIENT INFORMATION")
                
            # Check source info specific to this ingredient (stub logic)
            source_info_str = str(input_data.resource_source_information).lower() if input_data.resource_source_information else ""
            if term_name.lower() in source_info_str:
                if "origin" not in source_info_str:
                    signals.append("LIMITED RESOURCE SOURCE INFORMATION")
            else:
                signals.append("ORIGIN INFORMATION NOT PROVIDED")
                signals.append("ADDITIONAL REVIEW MAY BE APPROPRIATE")
                
            confidence_score = 30.0
            if matched_evidence: confidence_score += 40.0
            if "ORIGIN INFORMATION NOT PROVIDED" not in signals: confidence_score += 30.0
            
            level = "high" if confidence_score >= 80 else "moderate" if confidence_score >= 50 else "low"
            
            conf = ConfidenceIndicator(
                score=confidence_score,
                level=level,
                explanation="Confidence is based on the presence of ingredient-specific context and origin data.",
                limitations=["Per-ingredient source tracking may be incomplete."] if "ORIGIN INFORMATION NOT PROVIDED" in signals else []
            )
            
            results.append(ABSResourceAnalysis(
                ingredient=term.user_input,
                normalized_name=term_name,
                resource_context="Biological resource context derived from ingredient list.",
                available_source_information="Source information is incomplete or missing." if "ORIGIN INFORMATION NOT PROVIDED" in signals else "Source information available.",
                signals=signals,
                evidence_ids=[e.evidence_id for e in matched_evidence],
                confidence=conf
            ))
            
        return results
