import os
import json
from typing import Dict, List, Any
import google.generativeai as genai
from .provider import LLMProvider, StructuredResponse

class GeminiProvider(LLMProvider):
    def __init__(self):
        api_key = os.getenv("LLM_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        # Using a reasonable model for tasks
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        
    def generate_answer(self, prompt: str, system_prompt: str, context: str) -> StructuredResponse:
        full_prompt = f"System: {system_prompt}\n\nContext:\n{context}\n\nQuery:\n{prompt}\n\nRespond with ONLY a valid JSON object matching the requested schema."
        
        response = self.model.generate_content(
            full_prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
            ),
        )
        try:
            data = json.loads(response.text)
            return StructuredResponse(**data)
        except Exception as e:
            # Fallback for errors
            return StructuredResponse(
                answer="Error generating response.",
                language="English",
                query_type="ERROR",
                jurisdiction="Unknown",
                entities=[],
                citations=[],
                confidence="INSUFFICIENT EVIDENCE",
                evidence_gaps=[],
                limitations=[str(e)],
                recommended_next_steps=[],
                modules_used=[]
            )

    def generate_analysis(self, document_content: str, prompt: str) -> Dict[str, Any]:
        response = self.model.generate_content(
            f"Document:\n{document_content}\n\nTask:\n{prompt}\n\nReturn JSON.",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
            )
        )
        try:
            return json.loads(response.text)
        except:
            return {"error": "Failed to parse analysis JSON"}

    def summarize_evidence(self, evidences: List[str], query: str) -> str:
        content = "\n".join(evidences)
        response = self.model.generate_content(f"Summarize the following evidence for the query '{query}':\n\n{content}")
        return response.text

    def translate_response(self, text: str, target_language: str) -> str:
        response = self.model.generate_content(f"Translate the following text to {target_language}:\n\n{text}")
        return response.text

    def extract_entities(self, text: str) -> List[str]:
        response = self.model.generate_content(
            f"Extract Ayurvedic and IP entities from this text. Return a JSON list of strings.\n\nText: {text}",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
            )
        )
        try:
            return json.loads(response.text)
        except:
            return []

    def classify_query(self, query: str) -> str:
        categories = [
            "GENERAL_AYURVEDA", "TERMINOLOGY", "FORMULATION", "INTELLECTUAL_PROPERTY", 
            "PATENT", "TRADEMARK", "GEOGRAPHICAL_INDICATION", "TRADITIONAL_KNOWLEDGE", 
            "ABS", "REGULATORY", "JURISDICTION", "DOCUMENT_ANALYSIS", "RESEARCH", "OTHER"
        ]
        prompt = f"Classify this query into EXACTLY ONE of these categories: {', '.join(categories)}.\n\nQuery: {query}\n\nReturn only the category name."
        response = self.model.generate_content(prompt)
        cat = response.text.strip().upper()
        if cat in categories:
            return cat
        return "OTHER"
