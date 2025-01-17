from pydantic_settings import BaseSettings
from typing import List

def get_default_origins():
    return ["*"]

class Settings(BaseSettings):
    PROJECT_NAME: str = "PMP Question Generator API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "API para generar preguntas de examen PMP"

    # OpenAI
    OPENAI_API_KEY: str

    # Supabase
    SUPABASE_URL: str
    SUPABASE_KEY: str

    # CORS
    ALLOWED_ORIGINS: List[str] = None

    class Config:
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.ALLOWED_ORIGINS is None:
            self.ALLOWED_ORIGINS = ["*"]

settings = Settings()