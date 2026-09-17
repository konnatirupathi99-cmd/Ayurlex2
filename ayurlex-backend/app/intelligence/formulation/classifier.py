from typing import Dict, Any
from app.models.intelligence_output import ClassificationOutput

class FormulationClassifier:
    @staticmethod
    def classify(similarity_result: Dict[str, Any], confidence_score: float) -> ClassificationOutput:
        """
        Logic tree to classify the formulation.
        Prefers UNCLEAR if confidence is low.
        """
        pattern = similarity_result.get("pattern", "unclear")
        
        if confidence_score < 40.0 or pattern == "missing":
            return ClassificationOutput(
                type="unclear",
                label="Further Classification Required",
                summary="Available information is insufficient to confidently classify the formulation context."
            )
            
        if pattern == "classical":
            return ClassificationOutput(
                type="classical",
                label="Classical Context Identified",
                summary="Available information shows potential alignment with documented formulation references."
            )
            
        if pattern == "proprietary":
            return ClassificationOutput(
                type="proprietary",
                label="Proprietary Context Identified",
                summary="The available information suggests a customized or product-specific formulation context."
            )
            
        if pattern == "novel":
            return ClassificationOutput(
                type="potentially_novel",
                label="Potentially Novel Context",
                summary="Available evidence does not clearly identify a close formulation-level match. Additional prior-art and specialist review is recommended."
            )
            
        return ClassificationOutput(
            type="unclear",
            label="Further Classification Required",
            summary="Available information is insufficient to confidently classify the formulation context."
        )
