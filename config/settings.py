
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    api_key: str
    geo_url: str = "http://api.openweathermap.org/geo/1.0/direct"
    weather_url: str = "https://api.openweathermap.org/data/2.5/weather"
    request_timeout: int = 10
    lang: str = "ru"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
