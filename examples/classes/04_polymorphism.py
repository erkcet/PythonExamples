"""Method overriding and polymorphism in action."""


class Shape:
    """Base shape with area and describe methods."""

    def area(self):
        """Compute area (override in subclass)."""
        raise NotImplementedError

    def describe(self):
        """Describe the shape and its area."""
        return f"{self.__class__.__name__}: area = {self.area():.2f}"


class Circle(Shape):
    """Circle with radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """Rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    """Triangle with base and height."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
    for shape in shapes:
        print(shape.describe())
    total = sum(s.area() for s in shapes)
    print(f"Total area: {total:.2f}")
