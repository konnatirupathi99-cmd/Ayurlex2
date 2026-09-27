from typing import Any
from app.core.config import settings

def get_llm(temperature: float = 0.0, streaming: bool = False, provider: str = "openai", **kwargs: Any):
    """
    Returns a configured LLM instance based on the provider.
    This makes the model provider configurable so another LLM can be substituted without rewriting the application.
    """
    if provider.lower() == "openai":
        from langchain_community.chat_models import ChatOpenAI
        return ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model_name="gpt-4", # Default model
            temperature=temperature,
            streaming=streaming,
            **kwargs
        )
    # Example placeholder for Anthropic
    elif provider.lower() == "anthropic":
        from langchain_community.chat_models import ChatAnthropic
        return ChatAnthropic(
            anthropic_api_key="...",
            temperature=temperature,
            streaming=streaming,
            **kwargs
        )
        
    raise ValueError(f"Unsupported LLM provider: {provider}")
