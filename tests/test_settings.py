from pathlib import Path
from tempfile import TemporaryDirectory
from dotenv import load_dotenv
from _pytest.monkeypatch import MonkeyPatch  # импорт для типа

from config.settings import get_settings  # Импорт функции из проекта


def test_env_over_envfile(monkeypatch: MonkeyPatch) -> None:
    with TemporaryDirectory() as tmpdir:
        env_path = Path(tmpdir) / ".env"
        env_path.write_text("API_KEY=from_env_file\n")

        load_dotenv(env_path)

        monkeypatch.setenv("API_KEY", "from_env_variable")

        settings = get_settings()
        assert settings.api_key == "from_env_variable"

        monkeypatch.delenv("API_KEY")
        load_dotenv(env_path, override=True)

        settings2 = get_settings()
        assert settings2.api_key == "from_env_file"
