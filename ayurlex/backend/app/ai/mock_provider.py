import json
from typing import Dict, List, Any
from .provider import LLMProvider, StructuredResponse

class MockProvider(LLMProvider):
    def __init__(self):
        pass
        
    def generate_answer(self, prompt: str, system_prompt: str, context: str) -> StructuredResponse:
        return StructuredResponse(
            answer="This is a mocked response since no LLM_API_KEY is configured. AYURLEX retrieved the relevant evidence and formed this analysis based on your query: " + prompt,
            language="English",
            query_type="GENERAL_AYURVEDA",
            jurisdiction="India",
            entities=["Ayurveda"],
            citations=[],
            confidence="SUPPORTED BY EVIDENCE",
            evidence_gaps=["Mock provider cannot evaluate gaps."],
            limitations=["This is a mock response."],
            recommended_next_steps=["Configure a real LLM provider."],
            modules_used=["MockProvider"]
        )

    def generate_analysis(self, document_content: str, prompt: str) -> Dict[str, Any]:
        return {"analysis": "Mock analysis of document."}

    def summarize_evidence(self, evidences: List[str], query: str) -> str:
        return "Mock summary of evidence."

    def translate_response(self, text: str, target_language: str) -> str:
        return f"[Translated to {target_language}]: {text}"

    def extract_entities(self, text: str) -> List[str]:
        return ["MockEntity"]

    def classify_query(self, query: str) -> str:
        return "GENERAL_AYURVEDA"
