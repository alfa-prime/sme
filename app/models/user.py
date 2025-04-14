from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, UTC
from pydantic import EmailStr  # noqa
from app.models.enums import UserRole


class User(SQLModel, table=True):
    """
    Модель пользователя
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False, max_length=50)
    email: str = Field(index=True, unique=True, nullable=False, max_length=150)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    role: UserRole = Field(default=UserRole.user, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC), nullable=False)
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(UTC))
