import httpx
from fastapi import HTTPException, status
from config.settings import settings


async def get_coordinates(city: str) -> tuple[float, float]:
    params = {
        "q": city,
        "limit": 1,
        "appid": settings.api_key
    }

    async with httpx.AsyncClient(timeout=settings.request_timeout) as client:
        response = await client.get(settings.geo_url, params=params)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка внешнего API")

    data = response.json()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Город не найден")

    return data[0]["lat"], data[0]["lon"]


async def get_current_temperature(lat: float, lon: float) -> float:
    params = {
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "appid": settings.api_key,
        "lang": settings.lang
    }

    async with httpx.AsyncClient(timeout=settings.request_timeout) as client:
        response = await client.get(settings.weather_url, params=params)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка внешнего API")

    data = response.json()
    return data["main"]["temp"]
