from typing import Dict, List
from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import ModuleOutput

class LimitationDetector:
    @staticmethod
    def detect(input_data: IntelligenceInput, modules: Dict[str, ModuleOutput]) -> List[str]:
        """
        Detects limitations such as missing ingredients, conflicting evidence, or failed modules.
        """
        limitations = []
        
        if not input_data.ingredients:
            limitations.append("No ingredients provided in input.")
            
        if not input_data.jurisdiction:
            limitations.append("Missing jurisdiction information; analysis may lack local regulatory context.")
            
        for name, mod in modules.items():
            if mod.status == "failed":
                limitations.append(f"Module '{name}' failed during processing.")
            elif mod.status == "limited_evidence":
                limitations.append(f"Limited evidence available for '{name}' analysis.")
                
            limitations.extend(mod.limitations)
            
        return list(set(limitations)) # Deduplicate
