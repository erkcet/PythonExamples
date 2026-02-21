"""Dataclass with __slots__ for memory efficiency (Python 3.10+)."""

from dataclasses import dataclass
import sys


@dataclass(slots=True)
class SlottedPoint:
    """Memory-efficient point using slots."""
    x: float
    y: float
    z: float = 0.0

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


@dataclass
class RegularPoint:
    """Regular point without slots for comparison."""
    x: float
    y: float
    z: float = 0.0


def compare_memory():
    """Compare memory usage between slotted and regular dataclasses."""
    slotted = SlottedPoint(1.0, 2.0, 3.0)
    regular = RegularPoint(1.0, 2.0, 3.0)
    return {
        "slotted_size": sys.getsizeof(slotted),
        "regular_size": sys.getsizeof(regular),
        "has_dict": hasattr(regular, "__dict__"),
        "no_dict": not hasattr(slotted, "__dict__"),
    }


if __name__ == "__main__":
    p = SlottedPoint(3.0, 4.0, 5.0)
    print(f"Point: {p}")
    print(f"Magnitude: {p.magnitude():.2f}")
    print(f"Slots: {SlottedPoint.__slots__}")
    info = compare_memory()
    print(f"\nMemory comparison: {info}")
    try:
        p.w = 1.0
    except AttributeError as e:
        print(f"No dynamic attrs: {e}")
