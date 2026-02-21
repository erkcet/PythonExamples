"""Immutable (frozen) dataclasses."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Color:
    """An immutable color with RGB values."""
    red: int
    green: int
    blue: int

    def hex_code(self):
        return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"

    def brightness(self):
        return (self.red + self.green + self.blue) / 3


@dataclass(frozen=True)
class Coordinate:
    """An immutable geographic coordinate."""
    latitude: float
    longitude: float

    def __post_init__(self):
        if not -90 <= self.latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        if not -180 <= self.longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180")


if __name__ == "__main__":
    red = Color(255, 0, 0)
    print(f"Color: {red}, hex: {red.hex_code()}")
    print(f"Can be dict key: { {red: 'red'} }")
    try:
        red.red = 128
    except AttributeError as e:
        print(f"Immutable: {e}")
    nyc = Coordinate(40.7128, -74.0060)
    print(f"\nNYC: {nyc}")
    print(f"Hashable: {hash(nyc)}")
