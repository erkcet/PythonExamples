"""__slots__ for memory optimization and attribute restriction."""

import sys


class PointWithSlots:
    """Point using __slots__ for reduced memory footprint."""

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class PointWithoutSlots:
    """Regular Point with __dict__."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


def compare_memory():
    """Compare memory usage between slotted and regular classes."""
    slotted = PointWithSlots(1, 2)
    regular = PointWithoutSlots(1, 2)
    slot_size = sys.getsizeof(slotted)
    reg_size = sys.getsizeof(regular) + sys.getsizeof(regular.__dict__)
    return slot_size, reg_size


if __name__ == "__main__":
    p = PointWithSlots(3, 4)
    print(f"Slotted point: {p}")
    print(f"Slots: {PointWithSlots.__slots__}")

    try:
        p.z = 5
    except AttributeError as e:
        print(f"Cannot add attribute: {e}")

    slot_mem, reg_mem = compare_memory()
    print(f"Slotted size: {slot_mem} bytes")
    print(f"Regular size: ~{reg_mem} bytes")
