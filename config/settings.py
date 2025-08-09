import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, ValidationError

IS_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"

if not IS_GITHUB_ACTIONS:
    dotenv_path = Path(__file__).resolve().parent.parent / ".env"
    if dotenv_path.is_file():
        load_dotenv(dotenv_path)


class Settings(BaseSettings):
    api_key: str = Field(..., alias="API_KEY")
    geo_url: str = "http://api.openweathermap.org/geo/1.0/direct"
    weather_url: str = "https://api.openweathermap.org/data/2.5/weather"
    request_timeout: int = 10
    lang: str = "ru"

    model_config = SettingsConfigDict(
        populate_by_name=True,
    )


try:
    settings = Settings()
except ValidationError as e:
    raise RuntimeError(
        "Ошибка инициализации Settings: API_KEY не найден. "
        "Убедитесь, что переменная API_KEY задана в окружении или в .env"
    ) from e
