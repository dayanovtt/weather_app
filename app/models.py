from typing import Literal

from pydantic import BaseModel


class WeatherRequest(BaseModel):
    city: str
    scale: Literal["C", "F"]


class WeatherResponse(BaseModel):
    temperature: float
    scale: str
