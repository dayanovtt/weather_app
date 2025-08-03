import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from unittest.mock import AsyncMock, patch

from app.main import app


@pytest.mark.asyncio
@patch("app.main.get_coordinates", new_callable=AsyncMock)
@patch("app.main.get_current_temperature", new_callable=AsyncMock)
async def test_weather_fahrenheit(mock_temp, mock_coords):
    mock_coords.return_value = (55.75, 37.61)
    mock_temp.return_value = 25.0  # Температура в °C

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/weather", json={
            "city": "Москва",
            "scale": "F"
        })

    assert response.status_code == 200
    data = response.json()
    assert data["scale"] == "F"
    assert round(data["temperature"], 1) == round(25.0 * 9 / 5 + 32, 1)
