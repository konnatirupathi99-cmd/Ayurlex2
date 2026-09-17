import difflib
from typing import List, Set
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import TKTermAnalysis

class TKTermMatcher:
    @staticmethod
    def analyze(input_data: IntelligenceInput) -> TKTermAnalysis:
        """
        Validates the translation/normalization of user terms.
        Detects exact matches, aliases, and ambiguous mappings.
        """
        normalized_terms: Set[str] = set()
        ambiguous_terms: Set[str] = set()
        
        # We assume the AI synthesis/normalization layer populates normalized_ingredients
        for term in input_data.normalized_ingredients:
            if not term.normalized or term.normalized.lower() in ["unknown", "none", ""]:
                # Check for possible transliteration or fuzzy match issue
                # Here we could match against a known ontology, but for now we mark as ambiguous
                ambiguous_terms.add(term.user_input)
            else:
                normalized_terms.add(term.normalized)
                
                # Check if the user input is significantly different from normalized (alias/transliteration)
                similarity = difflib.SequenceMatcher(None, term.user_input.lower(), term.normalized.lower()).ratio()
                if similarity < 0.6 and term.user_input.lower() not in term.normalized.lower():
                    # It's an alias or translated term (e.g., Telugu to Sanskrit)
                    pass
        
        # Also check raw ingredients if they were missed by normalizer
        normalized_lower = {t.lower() for t in normalized_terms}
        for raw in input_data.ingredients:
            if raw.lower() not in normalized_lower:
                # Need to verify if it was normalized to something else
                found = False
                for term in input_data.normalized_ingredients:
                    if term.user_input.lower() == raw.lower():
                        found = True
                        break
                if not found:
                    ambiguous_terms.add(raw)
                    
        return TKTermAnalysis(
            normalized_terms=list(normalized_terms),
            ambiguous_terms=list(ambiguous_terms)
        )
