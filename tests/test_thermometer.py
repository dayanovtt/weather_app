import pytest
from app.thermometer import Thermometer

def test_to_frenheit():
    t = Thermometer(0)
    assert t.to_farenheit() == 32

    t = Thermometer(100)
    assert t.to_farenheit() == 212

def test_to_celsius():
    t = Thermometer(25.5)
    assert t.to_celsius() == 25.5