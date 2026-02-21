"""Overloading arithmetic and comparison operators."""


class Vector:
    """2D vector with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    a = Vector(1, 2)
    b = Vector(3, 4)
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * 3 = {a * 3}")
    print(f"3 * a = {3 * a}")
    print(f"|b| = {abs(b):.2f}")
    print(f"a == Vector(1,2): {a == Vector(1, 2)}")
