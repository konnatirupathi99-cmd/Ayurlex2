from typing import Dict, Any, Optional

class ManufacturingContextAnalyzer:
    def analyze(self, manufacturing_info: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        signals = []
        if not manufacturing_info:
            signals.append("MANUFACTURING INFORMATION LIMITED")
            return {"status": "needs_review", "signals": signals, "context": "Unknown"}
            
        signals.append("MANUFACTURING CONTEXT IDENTIFIED")
        
        info_str = str(manufacturing_info).lower()
        
        if "commercial" in info_str or "third-party" in info_str or "contract" in info_str:
            signals.append("COMMERCIAL DEVELOPMENT CONTEXT IDENTIFIED")
            signals.append("MANUFACTURING REVIEW MAY BE RELEVANT")
        elif "traditional" in info_str:
            signals.append("MANUFACTURING REVIEW MAY BE RELEVANT")
            
        return {
            "status": "completed",
            "signals": signals,
            "context": manufacturing_info
        }
