"""Using __post_init__ for validation and computed fields."""

from dataclasses import dataclass, field


@dataclass
class Temperature:
    """Temperature with automatic Fahrenheit conversion."""
    celsius: float
    fahrenheit: float = field(init=False)

    def __post_init__(self):
        self.fahrenheit = self.celsius * 9 / 5 + 32
        if self.celsius < -273.15:
            raise ValueError("Temperature below absolute zero")


@dataclass
class Rectangle:
    """Rectangle with computed area and perimeter."""
    width: float
    height: float
    area: float = field(init=False, repr=True)
    perimeter: float = field(init=False, repr=True)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)


if __name__ == "__main__":
    t = Temperature(100)
    print(f"{t.celsius}C = {t.fahrenheit}F")
    t2 = Temperature(0)
    print(f"{t2.celsius}C = {t2.fahrenheit}F")
    rect = Rectangle(5, 3)
    print(f"\n{rect}")
    try:
        Temperature(-300)
    except ValueError as e:
        print(f"Validation: {e}")
