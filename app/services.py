from typing import Tuple, Union
import httpx
from fastapi import HTTPException, status
from config.settings import settings

# Определяем тип для параметров запроса
ParamsType = dict[str, Union[str, int, float, bool, None]]


async def get_coordinates(city: str) -> Tuple[float, float]:
    params: ParamsType = {"q": city, "limit": 1, "appid": settings.api_key}

    async with httpx.AsyncClient(timeout=settings.request_timeout) as client:
        response = await client.get(settings.geo_url, params=params)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка внешнего API",
        )

    data = response.json()

    if not isinstance(data, list) or not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Город не найден",
        )

    lat = data[0].get("lat")
    lon = data[0].get("lon")

    if lat is None or lon is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Некорректные данные о городе",
        )

    return lat, lon


async def get_current_temperature(lat: float, lon: float) -> float:
    params: ParamsType = {
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "appid": settings.api_key,
        "lang": settings.lang,
    }

    async with httpx.AsyncClient(timeout=settings.request_timeout) as client:
        response = await client.get(settings.weather_url, params=params)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка внешнего API",
        )

    data = response.json()
    return float(data["main"]["temp"])
