"""DapurKu Configuration"""
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "DapurKu"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DATABASE_URL: str = "sqlite:///./dapurku.db"  # SQLite for MVP

    COMMISSION_RATE: float = 0.12
    PREMIUM_RATE: float = 0.03
    ADS_RATE: float = 0.02
    MIN_ORDER_AMOUNT: int = 15000

    class Config:
        env_file = ".env"

settings = Settings()
