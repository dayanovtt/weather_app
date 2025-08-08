
class Thermometer:
    def __init__(self, celsius_temp: float):
        self.celsius = celsius_temp

    def to_farenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    def to_celsius(self) -> float:
        return self.celsius

