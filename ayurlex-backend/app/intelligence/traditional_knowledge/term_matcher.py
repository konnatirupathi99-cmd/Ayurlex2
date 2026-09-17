from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import TKTermAnalysis

class TKTermMatcher:
    @staticmethod
    def analyze(input_data: IntelligenceInput) -> TKTermAnalysis:
        """
        Validates the translation/normalization of user terms.
        """
        normalized_terms = []
        ambiguous_terms = []
        
        for term in input_data.normalized_ingredients:
            if term.normalized and term.normalized.lower() != "unknown":
                normalized_terms.append(term.normalized)
            else:
                ambiguous_terms.append(term.user_input)
                
        return TKTermAnalysis(
            normalized_terms=normalized_terms,
            ambiguous_terms=ambiguous_terms
        )
