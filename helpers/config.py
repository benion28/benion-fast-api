from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from functools import lru_cache
import secrets


class Settings(BaseSettings):
    # Required
    DATABASE_URL: str
    SECRET_KEY: str

    # With defaults
    APP_NAME: str = "FastAPI Application"
    DEBUG: bool = False
    ENV: str = "development"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Email (Optional like Django os.getenv)
    EMAIL_HOST: str = "localhost"
    EMAIL_PORT: int = 25
    EMAIL_HOST_USER: str = ""
    EMAIL_HOST_PASSWORD: str = ""   # 👈 Django-style fallback
    EMAIL_USE_TLS: bool = False

    @field_validator("SECRET_KEY")
    def validate_secret(cls, v, info):
        if info.data.get("ENV") == "production" and not v:
            raise ValueError("SECRET_KEY is required in production")
        return v

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()
