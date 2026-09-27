from typing import List, Optional, Tuple
from app.multilingual.models import TerminologyMapping

class TerminologyEngine:
    def __init__(self):
        # Mock database for terminology mapping
        self._dictionary = {
            "ashwagandha": {
                "canonical": "Ashwagandha",
                "sanskrit": "अश्वगंधा",
                "hindi": "अश्वगंधा",
                "telugu": "అశ్వగంధ",
                "kannada": "ಅಶ್ವಗಂಧ",
                "tamil": "அசுவகந்தா",
                "malayalam": "അമുക്കുരം",
                "english": "Indian Ginseng",
                "scientific": "Withania somnifera",
                "synonyms": ["Winter cherry", "Amukkara"]
            },
            # Example of ambiguous term
            "brahmi": {
                "ambiguous": True,
                "matches": [
                    {
                        "canonical": "Bacopa monnieri",
                        "sanskrit": "ब्राह्मी",
                        "english": "Water Hyssop"
                    },
                    {
                        "canonical": "Centella asiatica",
                        "sanskrit": "मण्डूकपर्णी",
                        "english": "Gotu Kola"
                    }
                ]
            }
        }
        
    def analyze_term(self, original_term: str, detected_language: str = "en") -> TerminologyMapping:
        """
        Analyzes a term and maps it across languages and scientific nomenclatures.
        """
        term_lower = original_term.lower().strip()
        
        # Check if it's an exact match in our mock dictionary
        if term_lower in self._dictionary:
            entry = self._dictionary[term_lower]
            
            if entry.get("ambiguous"):
                # Handle ambiguity by NOT silently changing it
                return TerminologyMapping(
                    original_term=original_term,
                    canonical_term=original_term,
                    is_ambiguous=True,
                    possible_matches=[m["canonical"] for m in entry["matches"]]
                )
                
            # Exact mapping
            return TerminologyMapping(
                original_term=original_term,
                canonical_term=entry["canonical"],
                sanskrit_form=entry.get("sanskrit"),
                english_equivalent=entry.get("english"),
                scientific_name=entry.get("scientific"),
                synonyms=entry.get("synonyms", []),
                regional_variant=entry.get(detected_language)
            )
            
        # Fallback if unknown
        return TerminologyMapping(
            original_term=original_term,
            canonical_term=original_term
        )

terminology_engine = TerminologyEngine()
