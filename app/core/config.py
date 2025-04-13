from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database connection parameters
    DB_DRIVER: str = "postgresql+asyncpg"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "fastapi_admin"
    DATABASE_ECHO: bool = False

    @property
    def DATABASE_URL(self) -> str:
        """Construct database URL from components"""
        return (f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
