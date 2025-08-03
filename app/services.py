import httpx
from fastapi import HTTPException
from starlette.status import HTTP_200_OK
from config.settings import API_KEY


async def get_coordinates(city: str) -> tuple[float, float]:
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    params = {'q': city, 'limit': 1, 'appid': API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code != HTTP_200_OK:
        raise HTTPException(status_code=500, detail='Ошибка внешнего API')

    data = response.json()

    if not data:
        raise HTTPException(status_code=404, detail='Город не найден')

    lat = data[0]['lat']
    lon = data[0]['lon']

    return lat, lon


async def get_current_temperature(lat: float, lon: float) -> float:
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'appid': API_KEY,
        'lang': 'ru'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code != HTTP_200_OK:
        raise HTTPException(status_code=500, detail='Ошибка внешнего API')

    data = response.json()

    temp = data['main']['temp']

    return temp
