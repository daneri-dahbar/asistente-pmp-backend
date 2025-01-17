from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import questions, practice_sessions, auth, chat

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
)

# Configurar CORS - Manejar el string "*"
origins = [settings.ALLOWED_ORIGINS] if settings.ALLOWED_ORIGINS != "*" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(questions.router, prefix="/api", tags=["questions"])
app.include_router(practice_sessions.router, prefix="/api", tags=["practice-sessions"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])