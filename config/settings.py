import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, ValidationError


class Settings(BaseSettings):
    api_key: str = Field(..., alias="API_KEY")
    geo_url: str = "http://api.openweathermap.org/geo/1.0/direct"
    weather_url: str = "https://api.openweathermap.org/data/2.5/weather"
    request_timeout: int = 10
    lang: str = "ru"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
    )


def get_settings(api_key: Optional[str] = None) -> Settings:
    if api_key is not None:
        # передали явно api_key — создаём объект с ним
        return Settings(api_key=api_key)
    # иначе загрузка из env и .env файла
    return Settings()


try:
    settings = get_settings(api_key=os.getenv("API_KEY"))
except ValidationError as e:
    # Явно ругаемся если ключа нет
    raise RuntimeError("API_KEY not set in environment or .env") from e
