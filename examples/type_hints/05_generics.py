"""Generic types with TypeVar for reusable typed functions."""

from typing import TypeVar

T = TypeVar("T")
N = TypeVar("N", int, float)


def first(items: list[T]) -> T:
    """Return the first element of a list."""
    return items[0]


def maximum(a: N, b: N) -> N:
    """Return the larger of two numeric values."""
    return a if a >= b else b


class Stack(list[T]):
    """A typed stack built on list."""

    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self.append(item)

    def peek(self) -> T:
        """Return the top item without removing it."""
        return self[-1]


def demonstrate_generics():
    """Show TypeVar enabling generic, type-safe code."""
    print(f"first([1, 2, 3])     = {first([1, 2, 3])}")
    print(f"first(['a', 'b'])    = {first(['a', 'b'])}")
    print(f"maximum(10, 20)      = {maximum(10, 20)}")
    print(f"maximum(3.14, 2.71)  = {maximum(3.14, 2.71)}")

    stack: Stack[str] = Stack()
    for word in ("hello", "world"):
        stack.push(word)
    print(f"stack.peek() = {stack.peek()}")


if __name__ == "__main__":
    demonstrate_generics()
