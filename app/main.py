from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import questions, practice_sessions, auth, chat

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz para verificar que el servidor está funcionando
@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "PMP Question Generator API is running"
    }

# Incluir routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(questions.router, prefix="/api", tags=["questions"])
app.include_router(practice_sessions.router, prefix="/api", tags=["practice-sessions"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])