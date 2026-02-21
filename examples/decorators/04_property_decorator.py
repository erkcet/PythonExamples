"""@property for managed attribute access with getters and setters."""


class Temperature:
    """Temperature with Celsius storage and Fahrenheit property."""

    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature from Fahrenheit."""
        self.celsius = (value - 32) * 5 / 9

    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set Celsius with validation."""
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value


if __name__ == "__main__":
    t = Temperature(100)
    print(f"{t.celsius}°C = {t.fahrenheit}°F")
    t.fahrenheit = 32
    print(f"{t.celsius}°C = {t.fahrenheit}°F")
    try:
        t.celsius = -300
    except ValueError as e:
        print(f"Error: {e}")
