from supabase import create_client, Client
from app.core.config import settings
from app.models.user import UserCreate, UserInDB
from typing import Optional

class AuthService:
    def __init__(self):
        self.client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    async def signup(self, user_data: UserCreate) -> Optional[UserInDB]:
        try:
            response = self.client.auth.sign_up({
                "email": user_data.email,
                "password": user_data.password
            })
            if response.user:
                return UserInDB(
                    id=response.user.id,
                    email=response.user.email,
                    is_active=True
                )
            return None
        except Exception as e:
            print(f"Error en signup: {e}")
            return None

    async def login(self, email: str, password: str) -> Optional[dict]:
        try:
            response = self.client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            if response.user and response.session:
                return {
                    "user": UserInDB(
                        id=response.user.id,
                        email=response.user.email,
                        is_active=True
                    ),
                    "access_token": response.session.access_token,
                }
            return None
        except Exception as e:
            print(f"Error en login: {e}")
            return None

    async def get_current_user(self, token: str) -> Optional[UserInDB]:
        try:
            # En lugar de establecer la sesión, simplemente verificamos el token
            response = self.client.auth.get_user(token)
            if response and hasattr(response, 'user'):
                return UserInDB(
                    id=response.user.id,
                    email=response.user.email,
                    is_active=True
                )
            return None
        except Exception as e:
            print(f"Error obteniendo usuario actual: {e}")
            return None

auth_service = AuthService()