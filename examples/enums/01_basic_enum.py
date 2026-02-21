"""Basic enum usage in Python."""

from enum import Enum


class Color(Enum):
    """Basic color enumeration."""
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Direction(Enum):
    """Cardinal directions."""
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"

    def opposite(self):
        opposites = {self.NORTH: self.SOUTH, self.SOUTH: self.NORTH,
                     self.EAST: self.WEST, self.WEST: self.EAST}
        return opposites[self]


if __name__ == "__main__":
    print(f"Color.RED: {Color.RED}, value={Color.RED.value}, name={Color.RED.name}")
    print(f"By value: {Color(2)}")
    print(f"By name:  {Color['BLUE']}")
    print(f"All colors: {list(Color)}")
    print(f"Is enum: {isinstance(Color.RED, Color)}")
    d = Direction.NORTH
    print(f"\n{d} -> opposite: {d.opposite()}")
    print(f"Members: {[d.value for d in Direction]}")
