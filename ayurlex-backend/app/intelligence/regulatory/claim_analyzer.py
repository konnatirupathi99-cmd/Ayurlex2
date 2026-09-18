from typing import List, Dict, Any

class ClaimAnalyzer:
    def analyze(self, claims: List[str], intended_use: str) -> Dict[str, Any]:
        signals = []
        claim_types = set()
        
        if not claims and not intended_use:
            signals.append("CLAIM INFORMATION INCOMPLETE")
            return {"status": "needs_review", "signals": signals, "claim_types": list(claim_types)}
            
        combined_text = " ".join(claims).lower() + " " + (intended_use or "").lower()
        
        if any(word in combined_text for word in ["cure", "treat", "heal", "prevent", "disease", "health"]):
            claim_types.add("HEALTH-RELATED CLAIM")
            signals.append("HEALTH-RELATED CLAIM CONTEXT IDENTIFIED")
            signals.append("PRODUCT CLAIM REQUIRES FURTHER REVIEW")
            
        if any(word in combined_text for word in ["skin", "beauty", "glow", "hair", "complexion"]):
            claim_types.add("COSMETIC CLAIM")
            signals.append("CLAIM CONTEXT IDENTIFIED")
            
        if any(word in combined_text for word in ["traditional", "ancient", "ayurvedic"]):
            claim_types.add("TRADITIONAL USE CLAIM")
            
        if len(claim_types) > 1:
            signals.append("MULTIPLE CLAIM CONTEXTS IDENTIFIED")
            
        if not claim_types:
            signals.append("CLAIM CONTEXT IDENTIFIED")
            
        return {
            "status": "completed",
            "signals": signals,
            "claim_types": list(claim_types)
        }
