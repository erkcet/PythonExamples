"""Using collections.namedtuple for readable data records."""

from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", "red green blue")


def create_and_access():
    """Create namedtuples and access fields by name or index."""
    p = Point(3, 4)
    c = Color(red=255, green=128, blue=0)
    return p.x, p.y, p[0], c.red, c._asdict()


def distance(p1, p2):
    """Calculate distance between two Points."""
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def namedtuple_with_defaults():
    """Create namedtuple with default values."""
    Config = namedtuple("Config", ["host", "port", "debug"], defaults=["localhost", 8080, False])
    return Config(), Config(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    x, y, idx0, red, as_dict = create_and_access()
    print(f"Point: x={x}, y={y}, [0]={idx0}")
    print(f"Color as dict: {as_dict}")
    a, b = Point(0, 0), Point(3, 4)
    print(f"Distance {a}->{b}: {distance(a, b)}")
    default_cfg, custom_cfg = namedtuple_with_defaults()
    print(f"Default: {default_cfg}, Custom: {custom_cfg}")
