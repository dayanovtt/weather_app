from pydantic import BaseModel
from typing import Literal

class WeatherRequest(BaseModel):
     city: str
     scale: Literal['C', 'F']

class WeatherResponse(BaseModel):
    temperature: float
    scale: str

