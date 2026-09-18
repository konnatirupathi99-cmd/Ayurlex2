from typing import Dict, Any, Optional

class ProductFormAnalyzer:
    def analyze(self, product_form: Optional[str]) -> Dict[str, Any]:
        signals = []
        if not product_form:
            signals.append("PRODUCT FORM REQUIRES CLARIFICATION")
            return {"status": "needs_review", "signals": signals, "form_context": "Unknown"}
            
        form_lower = product_form.lower()
        
        signals.append("PRODUCT FORM CONTEXT AVAILABLE")
        
        if any(word in form_lower for word in ["tablet", "capsule", "syrup", "injection", "pill"]):
            signals.append("PRODUCT FORM MAY INFLUENCE REGULATORY REVIEW")
            form_context = "Pharmaceutical/Nutraceutical Form"
        elif any(word in form_lower for word in ["cream", "lotion", "oil", "topical"]):
            signals.append("PRODUCT FORM MAY INFLUENCE REGULATORY REVIEW")
            form_context = "Topical/Cosmetic Form"
        elif any(word in form_lower for word in ["powder", "food", "tea", "drink"]):
            form_context = "Food/Supplement Form"
        else:
            form_context = product_form
            
        return {
            "status": "completed",
            "signals": signals,
            "form_context": form_context
        }
