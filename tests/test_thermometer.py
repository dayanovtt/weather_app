import pytest
from app.temperature_converter import to_fahrenheit, to_celsius


@pytest.mark.parametrize("celsius, expected", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_to_fahrenheit(celsius, expected):
    assert to_fahrenheit(celsius) == expected


@pytest.mark.parametrize("celsius", [
    (0),
    (25.5),
    (-12.3),
])
def test_to_celsius(celsius):
    assert to_celsius(celsius) == celsius
