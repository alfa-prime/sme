from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  # noqa
from sqlalchemy.orm import sessionmaker  # noqa
from app.core.config import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    future=True
)

# ⬇️ DI-ready сессионная фабрика
async_session = sessionmaker(  # type: ignore
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# ⬇️ Провайдер для Depends(get_session)
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
