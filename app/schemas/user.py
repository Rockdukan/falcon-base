from pydantic import BaseModel, EmailStr


class UserCreatePayload(BaseModel):
    """Тело POST для создания пользователя в скелете."""
    email: EmailStr
    password: str
