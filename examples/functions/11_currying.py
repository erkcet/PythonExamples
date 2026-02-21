"""Currying in Python: transforming multi-arg functions into chains."""

from functools import wraps


def curry(func):
    """Decorator that curries a function of any arity."""
    @wraps(func)
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more: curried(*args, *more)
    return curried


@curry
def add(a, b):
    """Add two numbers."""
    return a + b


@curry
def multiply(a, b, c):
    """Multiply three numbers."""
    return a * b * c


def manual_curry_example():
    """Manually curried volume function."""
    def volume(length):
        def with_width(width):
            def with_height(height):
                return length * width * height
            return with_height
        return with_width
    return volume


if __name__ == "__main__":
    add5 = add(5)
    print(f"add5(3) = {add5(3)}")
    print(f"multiply(2)(3)(4) = {multiply(2)(3)(4)}")

    volume = manual_curry_example()
    print(f"volume(2)(3)(4) = {volume(2)(3)(4)}")
