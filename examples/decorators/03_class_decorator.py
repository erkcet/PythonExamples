"""Class-based decorators using __call__."""


class CountCalls:
    """Decorator that counts how many times a function is called."""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} time(s)")
        return self.func(*args, **kwargs)


class Enforce:
    """Decorator that enforces return type."""

    def __init__(self, return_type):
        self.return_type = return_type

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, self.return_type):
                raise TypeError(
                    f"Expected {self.return_type.__name__}, got {type(result).__name__}"
                )
            return result
        return wrapper


@CountCalls
def greet(name):
    """Greet someone."""
    return f"Hello, {name}!"


@Enforce(int)
def add(a, b):
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Bob"))
    print(f"Call count: {greet.count}")
    print(add(3, 4))
