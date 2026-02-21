"""Function basics: defining functions, default arguments, and return values."""


def greet(name, greeting="Hello"):
    """Return a greeting string with an optional custom greeting."""
    return f"{greeting}, {name}!"


def divide(a, b):
    """Return quotient and remainder as a tuple."""
    if b == 0:
        return None, None
    return a // b, a % b


def make_profile(name, age=25, city="Unknown"):
    """Build a profile dict with default values."""
    return {"name": name, "age": age, "city": city}


if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Bob", greeting="Hi"))

    quotient, remainder = divide(17, 5)
    print(f"17 / 5 = {quotient} remainder {remainder}")

    profile = make_profile("Eve", city="Paris")
    print(profile)
