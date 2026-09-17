from app.models.intelligence_input import IntelligenceInput
from app.models.intelligence_output import TrademarkContextOutput

class TrademarkContextAnalyzer:
    @staticmethod
    def analyze(input_data: IntelligenceInput) -> TrademarkContextOutput:
        """
        Analyzes innovation name for trademark context.
        """
        signals = []
        status = "Insufficient Naming Information"
        
        if input_data.innovation_name and input_data.innovation_name.lower() != "unknown":
            status = "Brand Name Review Recommended"
            signals.append("Potential Naming Similarity Requires Further Review")
        
        return TrademarkContextOutput(
            status=status,
            signals=signals
        )
