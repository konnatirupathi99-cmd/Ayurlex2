from typing import AsyncIterator
from app.ai.provider import get_llm
from app.ai.prompts import QA_PROMPT, ANALYSIS_PROMPT, SUMMARIZE_PROMPT, TRANSLATE_PROMPT, EXTRACT_PROMPT, CLASSIFY_PROMPT
from app.ai.schema import StructuredAIResponse, EntityExtraction, QueryClassification
from langchain_core.output_parsers import StrOutputParser

class AIService:
    def __init__(self, provider: str = "openai"):
        self.provider = provider

    async def generate_answer(self, query: str, evidence: str, history: str = "") -> StructuredAIResponse:
        """
        Accepts user question, retrieved evidence, and conversation context.
        Prioritizes retrieved authoritative evidence.
        Produces a structured AI response.
        """
        llm = get_llm(temperature=0.0, provider=self.provider)
        structured_llm = llm.with_structured_output(StructuredAIResponse)
        chain = QA_PROMPT | structured_llm
        
        return await chain.ainvoke({
            "query": query,
            "evidence": evidence,
            "history": history
        })

    async def generate_analysis(self, query: str, evidence: str, context: str = "") -> StructuredAIResponse:
        """
        Generates a deep analytical evaluation of IP or regulatory evidence.
        """
        llm = get_llm(temperature=0.2, provider=self.provider)
        structured_llm = llm.with_structured_output(StructuredAIResponse)
        chain = ANALYSIS_PROMPT | structured_llm
        
        return await chain.ainvoke({
            "query": query,
            "evidence": evidence,
            "context": context
        })

    async def summarize_evidence(self, evidence: str) -> str:
        """
        Summarizes authoritative evidence.
        """
        llm = get_llm(temperature=0.0, provider=self.provider)
        chain = SUMMARIZE_PROMPT | StrOutputParser()
        
        return await chain.ainvoke({"evidence": evidence})

    async def translate_response(self, text: str, target_language: str) -> str:
        """
        Translates text intelligently handling Ayurvedic and legal terminology.
        """
        llm = get_llm(temperature=0.1, provider=self.provider)
        chain = TRANSLATE_PROMPT | StrOutputParser()
        
        return await chain.ainvoke({"text": text, "target_language": target_language})

    async def extract_entities(self, text: str) -> EntityExtraction:
        """
        Extracts key entities (herbs, compounds, texts) from unstructured input.
        """
        llm = get_llm(temperature=0.0, provider=self.provider)
        structured_llm = llm.with_structured_output(EntityExtraction)
        chain = EXTRACT_PROMPT | structured_llm
        
        return await chain.ainvoke({"text": text})

    async def classify_query(self, query: str) -> QueryClassification:
        """
        Classifies the intent of the user query.
        """
        llm = get_llm(temperature=0.0, provider=self.provider)
        structured_llm = llm.with_structured_output(QueryClassification)
        chain = CLASSIFY_PROMPT | structured_llm
        
        return await chain.ainvoke({"query": query})

    async def stream_answer(self, query: str, evidence: str, history: str = "") -> AsyncIterator[str]:
        """
        Supports streaming for real-time frontend feedback.
        Note: Structured output streaming depends on the LLM capability. 
        This yields raw string chunks of the standard QA process.
        """
        llm = get_llm(temperature=0.0, streaming=True, provider=self.provider)
        chain = QA_PROMPT | StrOutputParser()
        
        async for chunk in chain.astream({
            "query": query,
            "evidence": evidence,
            "history": history
        }):
            yield chunk
