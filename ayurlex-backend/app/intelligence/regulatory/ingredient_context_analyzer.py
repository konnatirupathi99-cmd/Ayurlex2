from typing import List, Dict, Any
from app.models.responses import NormalizedTerm
from app.models.evidence import RetrievedEvidence
from app.models.intelligence_output import IngredientRegulatoryAnalysis, ConfidenceIndicator

class IngredientContextAnalyzer:
    def analyze(self, ingredients: List[str], normalized_ingredients: List[NormalizedTerm], evidence: List[RetrievedEvidence]) -> List[IngredientRegulatoryAnalysis]:
        results = []
        
        # Build mapping of ingredient to its normalized term if available
        normalized_map = {n.user_input: n for n in normalized_ingredients} if normalized_ingredients else {}
        
        for ing in ingredients:
            norm_term = normalized_map.get(ing)
            signals = []
            ing_evidence_ids = []
            
            # Find evidence related to this ingredient
            for e in evidence:
                if ing.lower() in e.content.lower() or (norm_term and norm_term.normalized.lower() in e.content.lower()):
                    ing_evidence_ids.append(e.evidence_id)
            
            regulatory_context = "Unknown"
            if not norm_term:
                signals.append("LIMITED INGREDIENT INFORMATION")
                signals.append("AMBIGUOUS INGREDIENT IDENTIFICATION")
            elif not ing_evidence_ids:
                signals.append("INSUFFICIENT EVIDENCE")
                regulatory_context = "Requires additional evidence"
            else:
                signals.append("RELEVANT INGREDIENT CONTEXT FOUND")
                regulatory_context = "Evidence available for review"
                
            results.append(IngredientRegulatoryAnalysis(
                ingredient=ing,
                normalized_name=norm_term.normalized if norm_term else "Unknown",
                scientific_name=norm_term.scientific if norm_term and hasattr(norm_term, 'scientific') else None,
                regulatory_context=regulatory_context,
                signals=signals,
                evidence_ids=ing_evidence_ids,
                confidence=ConfidenceIndicator(
                    score=0.6 if ing_evidence_ids else 0.3,
                    level="moderate" if ing_evidence_ids else "low",
                    explanation="Confidence is based on the availability of direct regulatory evidence.",
                    limitations=["Does not constitute regulatory approval of the ingredient."]
                )
            ))
            
        return results
