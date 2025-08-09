import pytest
from app.temperature_converter import to_celsius, to_fahrenheit


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0.0, 32.0),
        (100.0, 212.0),
        (-40.0, -40.0),
    ],
)
def test_to_fahrenheit(celsius: float, expected: float) -> None:
    assert to_fahrenheit(celsius) == expected


@pytest.mark.parametrize(
    "celsius",
    [
        0.0,
        25.5,
        -12.3,
    ],
)
def test_to_celsius(celsius: float) -> None:
    assert to_celsius(celsius) == celsius
