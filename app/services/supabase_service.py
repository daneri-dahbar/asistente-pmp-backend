from supabase import create_client
from typing import List
from app.core.config import settings
from app.models.practice_session import PracticeSession, PracticeSessionCreate


class SupabaseService:
    def __init__(self):
        self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    async def create_practice_session(self, session: PracticeSessionCreate) -> PracticeSession:
        response = self.client.table('practice_sessions').insert({
            'user_id': session.user_id,
            'start_time': session.start_time.isoformat(),
            'end_time': session.end_time.isoformat(),
            'personas_total': session.personas_total,
            'personas_correct': session.personas_correct,
            'proceso_total': session.proceso_total,
            'proceso_correct': session.proceso_correct,
            'entorno_total': session.entorno_total,
            'entorno_correct': session.entorno_correct
        }).execute()

        if len(response.data) == 0:
            raise ValueError("No se pudo crear la sesión de práctica")

        return PracticeSession(**response.data[0])

    async def get_practice_session(self, session_id: int) -> PracticeSession:
        response = self.client.table('practice_sessions').select('*').eq('id', session_id).execute()

        if len(response.data) == 0:
            raise ValueError(f"No se encontró la sesión con id {session_id}")

        return PracticeSession(**response.data[0])

    async def get_user_practice_sessions(self, user_id: str) -> List[PracticeSession]:
        """
        Obtiene todas las sesiones de práctica de un usuario específico
        """
        response = self.client.table('practice_sessions') \
            .select('*') \
            .eq('user_id', user_id) \
            .order('start_time', desc=True) \
            .execute()

        if len(response.data) == 0:
            raise ValueError(f"No se encontraron sesiones para el usuario {user_id}")

        return [PracticeSession(**session) for session in response.data]


supabase_service = SupabaseService()