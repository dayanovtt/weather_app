from fastapi import FastAPI, HTTPException

from app.models import WeatherResponse, WeatherRequest
from app.services import get_coordinates, get_current_temperature
from app.thermometer import Thermometer



app = FastAPI()


@app.post('/weather', response_model=WeatherResponse)
async def get_weather(req: WeatherRequest):
    lat, lon = await get_coordinates(req.city)
    temp_c = await get_current_temperature(lat, lon)

    thermometer = Thermometer(temp_c)

    if req.scale == 'F':
        temp = thermometer.to_farenheit()
    else:
        temp = thermometer.to_celsius()

    return WeatherResponse(temperature=round(temp, 1), scale=req.scale)
