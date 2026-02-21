"""Simple function decorator that wraps a function with extra behavior."""

from functools import wraps


def log_calls(func):
    """Decorator that logs function calls and return values."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"-> Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"<- {func.__name__} returned {result}")
        return result
    return wrapper


@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b


@log_calls
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    add(3, 4)
    greet("Alice")
    print(f"Preserved name: {greet.__name__}")
    print(f"Preserved doc: {greet.__doc__}")
