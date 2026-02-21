"""Protocol classes for structural subtyping (duck typing with types)."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    """Any object with a draw() -> str method."""
    def draw(self) -> str: ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    def draw(self) -> str:
        return f"Circle(r={self.radius})"


class Square:
    def __init__(self, side: float):
        self.side = side
    def draw(self) -> str:
        return f"Square(s={self.side})"


def render(shape: Drawable) -> None:
    """Render any Drawable shape. No inheritance required."""
    print(f"  Rendering: {shape.draw()}")


def demonstrate_protocols():
    """Show structural subtyping with Protocol."""
    shapes = [Circle(5.0), Square(3.0)]
    for shape in shapes:
        print(f"Is Drawable? {isinstance(shape, Drawable)}")
        render(shape)


if __name__ == "__main__":
    demonstrate_protocols()
