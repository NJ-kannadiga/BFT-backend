from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="Finance Tracker API")
    DEBUG: bool = Field(default=True)
    DATABASE_URL: str = Field(default="postgresql://postgres:postgres@localhost:5432/finance_db")
    SECRET_KEY: str = Field(default="change-me-to-a-strong-secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24)

    class Config:
        env_file = ".env"

settings = Settings()
