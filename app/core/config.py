from pydantic_settings import BaseSettings

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
    ALLOWED_ORIGINS: str = "*"

    class Config:
        env_file = ".env"

settings = Settings()