from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock

from app.main import app

client = TestClient(app)


def test_weather_fahrenheit():
    with patch("app.main.get_coordinates", new_callable=AsyncMock) as mock_coords, \
         patch("app.main.get_current_temperature", new_callable=AsyncMock) as mock_temp:

        mock_coords.return_value = (55.75, 37.61)
        mock_temp.return_value = 25.0

        response = client.post("/weather", json={
            "city": "Москва",
            "scale": "F"
        })

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["scale"] == "F"
        assert round(data["temperature"], 1) == round(25.0 * 9 / 5 + 32, 1)
