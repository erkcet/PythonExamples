"""Dataclass field defaults and factories."""

from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class ShoppingCart:
    """Shopping cart with field defaults and factories."""
    owner: str
    items: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    _total: float = field(default=0.0, repr=False, compare=False)

    def add_item(self, item):
        self.items.append(item)


@dataclass
class Config:
    """Configuration with various field options."""
    name: str
    debug: bool = False
    max_retries: int = field(default=3, metadata={"help": "Max retry attempts"})
    tags: List[str] = field(default_factory=list)
    _id: int = field(default_factory=lambda: id(object()), repr=False)


if __name__ == "__main__":
    cart1 = ShoppingCart("Alice")
    cart2 = ShoppingCart("Bob")
    cart1.add_item("apple")
    print(f"Cart 1: {cart1}")
    print(f"Cart 2: {cart2}")
    print(f"Lists independent: {cart1.items is not cart2.items}")
    cfg = Config("myapp", tags=["prod"])
    print(f"\nConfig: {cfg}")
    print(f"Metadata: {Config.__dataclass_fields__['max_retries'].metadata}")
