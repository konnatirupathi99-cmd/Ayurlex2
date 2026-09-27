from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    PROJECT_NAME: str = "AYURLEX Backend"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Environment (development, staging, production)
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    
    # Secrets
    SECRET_KEY: str = "super-secret-key-for-dev"
    
    # DB / Redis / etc
    DATABASE_URL: str = "sqlite:///./ayurlex.db"
    
    # Extra fields
    OPENAI_API_KEY: str = "mock-key-for-prototype"
    CHROMA_DB_PATH: str = "./chroma_db"
    UPLOADS_DIR: str = "./uploads"
    MOCK_LLM_RESPONSES: bool = True
    
    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()
