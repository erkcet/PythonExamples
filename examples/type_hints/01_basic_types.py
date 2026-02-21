"""Basic type hints: int, str, float, bool annotations."""


def greet(name: str, excited: bool = False) -> str:
    """Return a greeting for the given name."""
    base = f"Hello, {name}"
    return f"{base}!" if excited else f"{base}."


def bmi(weight_kg: float, height_m: float) -> float:
    """Calculate body mass index."""
    return weight_kg / (height_m ** 2)


def repeat_char(char: str, count: int) -> str:
    """Repeat a character count times."""
    return char * count


def demonstrate_basic_types():
    """Show functions with basic type annotations."""
    print(greet("Alice"))
    print(greet("Bob", excited=True))
    print(f"BMI: {bmi(70.0, 1.75):.1f}")
    print(repeat_char("*", 20))

    # Type hints are not enforced at runtime
    age: int = 30
    name: str = "Carol"
    active: bool = True
    print(f"{name}, age {age}, active={active}")


if __name__ == "__main__":
    demonstrate_basic_types()
