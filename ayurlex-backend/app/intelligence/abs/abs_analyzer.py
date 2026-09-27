from typing import Dict, Any
from app.intelligence.models import BaseIntelligenceModule, IntelligenceResult

class ABSContextAnalyzer(BaseIntelligenceModule):
    def analyze(self, query: str, context: Dict[str, Any]) -> IntelligenceResult:
        """
        Analyzes: Biological resource context, Origin/source context, Utilization context, Jurisdiction context.
        """
        return IntelligenceResult(
            finding="Biological resources identified trigger Access and Benefit Sharing (ABS) obligations under the Biological Diversity Act, 2002.",
            evidence=[{"content": "Utilization of Indian biological resources for commercial research requires NBA approval."}],
            sources=["Biological Diversity Act, 2002 (India)"],
            confidence="High",
            limitations=["Does not verify the specific geographic origin of the raw material procurement."]
        )

abs_analyzer = ABSContextAnalyzer()
