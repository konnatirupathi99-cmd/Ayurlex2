from typing import Dict, Any, Optional

class JurisdictionContextAnalyzer:
    def analyze(self, jurisdiction: Optional[str]) -> Dict[str, Any]:
        signals = []
        if not jurisdiction:
            signals.append("JURISDICTION NOT SPECIFIED")
            return {"status": "needs_review", "signals": signals, "context": "Unknown"}
            
        j_lower = jurisdiction.lower()
        
        if "india" in j_lower:
            signals.append("JURISDICTION-SPECIFIC REVIEW RECOMMENDED")
            context = "India"
        elif "international" in j_lower:
            context = "International"
        else:
            context = jurisdiction
            
        return {
            "status": "completed",
            "signals": signals,
            "context": context
        }
