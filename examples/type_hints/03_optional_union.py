"""Optional and Union types for flexible function signatures."""

from typing import Optional, Union


def find_user(user_id: int) -> Optional[str]:
    """Look up a user, returning None if not found."""
    users = {1: "Alice", 2: "Bob", 3: "Carol"}
    return users.get(user_id)


def format_value(value: Union[int, float, str]) -> str:
    """Format different types into a display string."""
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def safe_divide(a: float, b: float) -> Optional[float]:
    """Divide a by b, returning None instead of raising."""
    if b == 0:
        return None
    return a / b


def demonstrate_optional_union():
    """Show Optional and Union in action."""
    for uid in (1, 2, 99):
        name = find_user(uid)
        print(f"User {uid}: {name if name else 'NOT FOUND'}")

    for val in (42, 3.14159, "hello"):
        print(f"format_value({val!r}) -> {format_value(val)}")

    print(f"10 / 3 = {safe_divide(10, 3)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")


if __name__ == "__main__":
    demonstrate_optional_union()
