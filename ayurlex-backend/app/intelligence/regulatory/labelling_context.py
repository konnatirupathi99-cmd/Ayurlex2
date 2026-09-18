from typing import Dict, Any, Optional

class LabellingContextAnalyzer:
    def analyze(self, labelling_info: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        signals = []
        if not labelling_info:
            signals.append("LABELLING INFORMATION NOT PROVIDED")
            return {"status": "needs_review", "signals": signals, "context": {}}
            
        signals.append("LABELLING CONTEXT AVAILABLE")
        
        info_str = str(labelling_info).lower()
        if "claim" in info_str or "intended" in info_str:
            signals.append("PRODUCT CLAIMS MAY REQUIRE REVIEW")
            
        if "warning" not in info_str:
            signals.append("FURTHER LABELLING REVIEW MAY BE APPROPRIATE")
            
        return {
            "status": "completed",
            "signals": signals,
            "context": labelling_info
        }
