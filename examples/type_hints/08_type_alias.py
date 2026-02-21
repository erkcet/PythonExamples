"""Type aliases and NewType for semantic clarity."""

from typing import NewType

# Simple type aliases for readability
Vector = list[float]
Matrix = list[Vector]
Headers = dict[str, str]

# NewType creates distinct types for the type checker
UserId = NewType("UserId", int)
EmailAddr = NewType("EmailAddr", str)


def dot_product(a: Vector, b: Vector) -> float:
    """Compute dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))


def transpose(matrix: Matrix) -> Matrix:
    """Transpose a matrix (list of row vectors)."""
    return [list(row) for row in zip(*matrix)]


def send_email(to: EmailAddr, subject: str) -> str:
    """Simulate sending an email (NewType for safety)."""
    return f"Sent '{subject}' to {to}"


def demonstrate_aliases():
    """Show type aliases and NewType in practice."""
    v1: Vector = [1.0, 2.0, 3.0]
    v2: Vector = [4.0, 5.0, 6.0]
    print(f"Dot product: {dot_product(v1, v2)}")

    m: Matrix = [[1, 2], [3, 4], [5, 6]]
    print(f"Transposed:  {transpose(m)}")

    addr = EmailAddr("alice@example.com")
    print(send_email(addr, "Hello"))


if __name__ == "__main__":
    demonstrate_aliases()
