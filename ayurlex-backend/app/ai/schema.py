from pydantic import BaseModel, Field
from typing import List

class StructuredAIResponse(BaseModel):
    answer: str = Field(description="The detailed main response to the user's query. Distinguish clearly between evidence and interpretation.")
    language: str = Field(description="The language of the response.")
    citations: List[str] = Field(description="Exact citations from the provided evidence used in the answer. Never invent these.")
    confidence: str = Field(description="Confidence level based on the evidence provided (e.g., 'High', 'Medium', 'Low').")
    evidence_gaps: List[str] = Field(description="Information missing from the provided evidence to fully answer the query.")
    limitations: List[str] = Field(description="Limitations of the current analysis.")
    recommended_next_steps: List[str] = Field(description="Recommended next steps for the user.")

class EntityExtraction(BaseModel):
    entities: List[str] = Field(description="List of extracted entities (e.g., herbs, active compounds, regulations).")

class QueryClassification(BaseModel):
    intent: str = Field(description="The classification intent (e.g., 'ip_analysis', 'regulatory_compliance', 'formulation_check', 'general').")
    primary_language: str = Field(description="The primary language of the user query.")
