"""Enums with custom methods and properties."""

from enum import Enum


class Suit(Enum):
    """Playing card suits with rich behavior."""
    HEARTS = ("H", "red", "\u2665")
    DIAMONDS = ("D", "red", "\u2666")
    CLUBS = ("C", "black", "\u2663")
    SPADES = ("S", "black", "\u2660")

    def __init__(self, code, color, symbol):
        self.code = code
        self.color = color
        self.symbol = symbol

    def is_red(self):
        return self.color == "red"

    def __str__(self):
        return f"{self.symbol} {self.name.title()}"


class HTTPMethod(Enum):
    """HTTP methods with metadata."""
    GET = ("safe", True)
    POST = ("unsafe", False)
    PUT = ("unsafe", True)
    DELETE = ("unsafe", True)

    def __init__(self, safety, idempotent):
        self.safety = safety
        self.idempotent = idempotent

    @property
    def is_safe(self):
        return self.safety == "safe"


if __name__ == "__main__":
    print("Card suits:")
    for s in Suit:
        print(f"  {s} (code={s.code}, red={s.is_red()})")
    print(f"\nHTTP Methods:")
    for m in HTTPMethod:
        print(f"  {m.name}: safe={m.is_safe}, idempotent={m.idempotent}")
