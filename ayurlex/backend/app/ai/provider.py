from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from pydantic import BaseModel

class StructuredResponse(BaseModel):
    answer: str
    language: str
    query_type: str
    jurisdiction: str
    entities: List[str]
    citations: List[Dict[str, Any]]
    confidence: str
    evidence_gaps: List[str]
    limitations: List[str]
    recommended_next_steps: List[str]
    modules_used: List[str]

class LLMProvider(ABC):
    
    @abstractmethod
    def generate_answer(self, prompt: str, system_prompt: str, context: str) -> StructuredResponse:
        pass
        
    @abstractmethod
    def generate_analysis(self, document_content: str, prompt: str) -> Dict[str, Any]:
        pass
        
    @abstractmethod
    def summarize_evidence(self, evidences: List[str], query: str) -> str:
        pass
        
    @abstractmethod
    def translate_response(self, text: str, target_language: str) -> str:
        pass
        
    @abstractmethod
    def extract_entities(self, text: str) -> List[str]:
        pass
        
    @abstractmethod
    def classify_query(self, query: str) -> str:
        pass
