"""Basic dataclass usage."""

from dataclasses import dataclass, asdict, astuple


@dataclass
class Point:
    """A 2D point."""
    x: float
    y: float

    def distance_to(self, other):
        """Euclidean distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass
class Person:
    """A person with name and age."""
    name: str
    age: int
    email: str = ""

    def greet(self):
        return f"Hi, I'm {self.name}, age {self.age}"


if __name__ == "__main__":
    p1 = Point(3.0, 4.0)
    p2 = Point(0.0, 0.0)
    print(f"Point: {p1}")
    print(f"Distance to origin: {p1.distance_to(p2):.2f}")
    print(f"As dict: {asdict(p1)}")
    print(f"As tuple: {astuple(p1)}")
    person = Person("Alice", 30, "alice@example.com")
    print(f"\n{person}")
    print(person.greet())
    print(f"Equality: {Person('Bob', 25) == Person('Bob', 25)}")
