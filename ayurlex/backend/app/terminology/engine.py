from typing import Dict, Any, List

class TerminologyEngine:
    def __init__(self):
        # Seed terminology database
        self.terminology_db = {
            "ashwagandha": {
                "original_term": "Ashwagandha",
                "canonical_term": "Ashwagandha",
                "scientific_name": "Withania somnifera",
                "hindi_name": "अश्वगंधा",
                "telugu_name": "అశ్వగంధ",
                "sanskrit_name": "Ashvagandha",
                "synonyms": ["Indian Ginseng", "Winter Cherry"],
                "confidence": "HIGH"
            },
            "turmeric": {
                "original_term": "Turmeric",
                "canonical_term": "Turmeric",
                "scientific_name": "Curcuma longa",
                "hindi_name": "हल्दी (Haldi)",
                "telugu_name": "పసుపు (Pasupu)",
                "sanskrit_name": "Haridra",
                "synonyms": ["Curcumin"],
                "confidence": "HIGH"
            }
        }
        
    def lookup_ayurvedic_term(self, term: str) -> List[Dict[str, Any]]:
        term_lower = term.lower()
        results = []
        for key, data in self.terminology_db.items():
            if term_lower in key or term_lower in data["canonical_term"].lower() or \
               any(term_lower in syn.lower() for syn in data["synonyms"]) or \
               term_lower in data["scientific_name"].lower() or \
               term_lower in data.get("telugu_name", "").lower() or \
               term_lower in data.get("hindi_name", "").lower():
                results.append(data)
                
        return results
