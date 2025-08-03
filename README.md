# Weather Service API

## 1. Описание проекта, установка и запуск

Этот проект — backend-сервис на FastAPI, который принимает название города и возвращает текущую температуру в выбранной температурной шкале (Цельсий или Фаренгейт). Температура получается из OpenWeatherMap API.

### Функционал и особенности:
- Асинхронные HTTP-запросы к OpenWeatherMap с помощью `httpx`.
- Валидация данных через Pydantic.
- Юнит-тесты с `pytest` и мокирование внешних вызовов.
- CI/CD с GitHub Actions.
- Управление переменными окружения через `.env`.

### Установка и запуск:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/dayanovtt/weather_app.git
   cd Weather
   
2. Создайте и активируйте виртуальное окружение:
    ```bash
      python3 -m venv venv
      source venv/bin/activate   # Linux/MacOS
      venv\Scripts\activate      # Windows

3. Установите зависимости:
    ```bash
   pip install -r requirements.txt

4. Создайте файл .env в корне проекта и добавьте:
    ```ini
   OPENWEATHER_API_KEY=ваш_api_ключ

5. Запустите сервер:
    ```bash
   uvicorn app.main:app --reload

6. Откройте http://localhost:8000/docs для тестирования API через Swagger UI.

## 2. Использование API
Метод: POST /weather

    Тело запроса (JSON):

```json
{
  "city": "Москва",
  "scale": "F"  // "C" или "F"
}

```

    Ответ:
```json
{
  "city": "Москва",
  "temperature": 77.0,
  "scale": "F"
}

```

    Тестирование:
```bash
    pytest
```

## 4. CI/CD
В проекте настроен GitHub Actions workflow .github/workflows/python-app.yml, который автоматически запускает тесты при пуше и pull request в ветку main.


## 5. Стек технологий
Python 3.12

FastAPI

httpx

Pydantic

pytest, pytest-asyncio

GitHub Actions

## 6. Контакты
Если есть вопросы или предложения — пишите!
