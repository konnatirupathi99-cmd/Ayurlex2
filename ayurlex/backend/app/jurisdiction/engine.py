from typing import Dict, Any, List

class JurisdictionEngine:
    def __init__(self):
        self.jurisdictions = {
            "india": {
                "country": "India",
                "authority": "Ministry of Ayush / Indian Patent Office",
                "scope": "National",
                "key_acts": ["Drugs and Cosmetics Act, 1940", "Indian Patents Act, 1970 (Sec 3p)"]
            },
            "us": {
                "country": "United States",
                "authority": "USPTO / FDA",
                "scope": "National",
                "key_acts": ["DSHEA 1994"]
            }
        }
        
    def lookup_jurisdiction(self, text: str) -> List[Dict[str, Any]]:
        text_lower = text.lower()
        results = []
        if "india" in text_lower or "indian" in text_lower or "ayush" in text_lower:
            results.append(self.jurisdictions["india"])
        if "us" in text_lower or "united states" in text_lower or "uspto" in text_lower or "fda" in text_lower:
            results.append(self.jurisdictions["us"])
            
        if not results:
            results.append({"country": "International/General", "scope": "Global"})
            
        return results
