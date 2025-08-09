from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# Загружаем .env, если он есть (только локально)
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


# Просто создаём Settings — pydantic подхватит API_KEY из os.environ (уже с alias)
settings = Settings()
