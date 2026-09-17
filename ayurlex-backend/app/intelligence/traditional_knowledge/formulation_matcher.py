from typing import List, Set
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import TKFormulationAnalysis
from app.intelligence.traditional_knowledge.models import TKEvidenceContext

class TKFormulationMatcher:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[TKEvidenceContext]) -> TKFormulationAnalysis:
        """
        Analyzes formulation-level similarity as opposed to ingredient-level similarity.
        """
        signals: Set[str] = set()
        matched_evidence_ids: Set[str] = set()
        
        ingredient_names = [ing.normalized.lower() for ing in input_data.normalized_ingredients if ing.normalized]
        ingredient_names.extend([ing.lower() for ing in input_data.ingredients])
        ingredient_names = list(set(ingredient_names))
        
        form_context_str = str(input_data.formulation_context).lower() if input_data.formulation_context else ""
        
        for e in evidence:
            text = (e.relevant_excerpt + " " + e.source_title).lower()
            
            # Count how many ingredients are mentioned in this specific piece of evidence
            matched_ingredients = sum(1 for ing in ingredient_names if ing in text)
            
            if matched_ingredients > 1:
                matched_evidence_ids.add(e.evidence_id)
                if matched_ingredients == len(ingredient_names) and len(ingredient_names) > 0:
                    signals.add("Potential Formulation-Level Similarity")
                else:
                    signals.add("Partial Ingredient-Level Overlap")
                    
            # Check preparation/formulation context match (e.g., kwatha, churna)
            if form_context_str and any(prep in text for prep in ["decoction", "powder", "oil", "ghee", "paste", "kwatha", "churna", "taila", "ghrita"]):
                if any(prep in form_context_str for prep in ["decoction", "powder", "oil", "ghee", "paste", "kwatha", "churna", "taila", "ghrita"]):
                    signals.add("Related Traditional Preparation Context")
                    matched_evidence_ids.add(e.evidence_id)

        if not matched_evidence_ids:
            signals.add("Limited Formulation-Level Evidence")
            signals.add("No Clear Close Match Retrieved")
            
        return TKFormulationAnalysis(
            signals=list(signals),
            evidence_ids=list(matched_evidence_ids)
        )
