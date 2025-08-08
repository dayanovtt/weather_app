from fastapi import FastAPI

from app.models import WeatherResponse, WeatherRequest
from app.services import get_coordinates, get_current_temperature
from app.temperature_converter import to_fahrenheit, to_celsius

app = FastAPI()


@app.post("/weather", response_model=WeatherResponse)
async def get_weather(req: WeatherRequest):
    lat, lon = await get_coordinates(req.city)
    temp_c = await get_current_temperature(lat, lon)

    if req.scale == "F":
        temp = to_fahrenheit(temp_c)
    else:
        temp = to_celsius(temp_c)

    return WeatherResponse(temperature=round(temp, 1), scale=req.scale)
