from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    api_key: Optional[str] = Field(None, alias="API_KEY")
    geo_url: str = "http://api.openweathermap.org/geo/1.0/direct"
    weather_url: str = "https://api.openweathermap.org/data/2.5/weather"
    request_timeout: int = 10
    lang: str = "ru"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
    )


settings = Settings()

if not settings.api_key:
    raise RuntimeError("API_KEY is not set in environment variables or .env file")
