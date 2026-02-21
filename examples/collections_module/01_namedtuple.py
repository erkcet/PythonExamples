"""namedtuple usage for lightweight immutable data structures."""

from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", "red green blue")
Employee = namedtuple("Employee", "name department salary", defaults=["Unknown", 0])


def distance(p1, p2):
    """Calculate distance between two Points."""
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


def employee_from_dict(data):
    """Create an Employee from a dictionary."""
    return Employee(**data)


if __name__ == "__main__":
    p1, p2 = Point(3, 4), Point(6, 8)
    print(f"Points: {p1}, {p2}")
    print(f"Distance: {distance(p1, p2):.2f}")
    print(f"X of p1: {p1.x}, via index: {p1[0]}")

    red = Color(255, 0, 0)
    print(f"\nColor: {red}, as dict: {red._asdict()}")

    emp = employee_from_dict({"name": "Alice", "department": "Eng", "salary": 90000})
    print(f"Employee: {emp}")
    updated = emp._replace(salary=95000)
    print(f"After raise: {updated}")
    print(f"Fields: {Employee._fields}")
