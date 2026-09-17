from typing import List, Set
from app.models.intelligence_input import IntelligenceInput

class ABSResourceContextAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput) -> List[str]:
        """
        Identifies general biological resource context.
        """
        signals: Set[str] = set()
        
        # Check if they explicitly provided biological_resources
        if input_data.biological_resources:
            signals.add("BIOLOGICAL RESOURCE CONTEXT IDENTIFIED")
        
        # Check if ingredients exist (we assume most ayurvedic ingredients are biological/natural)
        if input_data.ingredients:
            signals.add("NATURAL INGREDIENT CONTEXT IDENTIFIED")
            
        if input_data.resource_source_information:
            signals.add("RESOURCE INFORMATION AVAILABLE")
            
            # Simple check if source location is mentioned
            source_str = str(input_data.resource_source_information).lower()
            if "origin" not in source_str and "location" not in source_str:
                signals.add("RESOURCE SOURCE INFORMATION LIMITED")
        else:
            if input_data.ingredients or input_data.biological_resources:
                signals.add("FURTHER RESOURCE CONTEXT REVIEW MAY BE REQUIRED")
                
        return list(signals)
