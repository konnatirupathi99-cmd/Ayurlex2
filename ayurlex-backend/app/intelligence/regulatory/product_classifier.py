from typing import List, Dict, Any
from app.models.intelligence_output import ProductClassificationOutput, ConfidenceIndicator

class ProductClassifier:
    def analyze(self, product_type: str, intended_use: str, description: str) -> ProductClassificationOutput:
        contexts = []
        signals = []
        
        combined_text = f"{product_type} {intended_use} {description}".lower()
        
        if "cosmetic" in combined_text or "skin" in combined_text:
            contexts.append("COSMETIC")
        if "herb" in combined_text or "wellness" in combined_text:
            contexts.append("HERBAL WELLNESS PRODUCT")
        if "ayurved" in combined_text:
            contexts.append("AYURVEDIC PRODUCT")
        if "food" in combined_text or "diet" in combined_text or "nutrition" in combined_text:
            contexts.append("FOOD / AYURVEDA AAHAR")
            
        if not contexts:
            contexts.append("FURTHER CLASSIFICATION REQUIRED")
            signals.append("INSUFFICIENT PRODUCT INFORMATION")
        elif len(contexts) > 1:
            signals.append("MULTIPLE PRODUCT CONTEXTS POSSIBLE")
        else:
            signals.append("POTENTIAL PRODUCT CATEGORY IDENTIFIED")
            
        return ProductClassificationOutput(
            potential_contexts=contexts,
            signals=signals,
            confidence=ConfidenceIndicator(
                score=0.7,
                level="moderate",
                explanation="Classification based on heuristic text matching.",
                limitations=["Automated classification is not a final regulatory determination."]
            )
        )
