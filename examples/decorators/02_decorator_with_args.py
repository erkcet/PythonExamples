"""Decorator that accepts arguments via a decorator factory."""

from functools import wraps


def repeat(n):
    """Decorator factory: repeat a function call n times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


def tag(tag_name):
    """Decorator factory: wrap return value in an HTML tag."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag_name}>{result}</{tag_name}>"
        return wrapper
    return decorator


@repeat(3)
def say_hello(name):
    """Greet someone."""
    return f"Hello, {name}!"


@tag("strong")
@tag("em")
def emphasize(text):
    """Emphasize text."""
    return text


if __name__ == "__main__":
    print(say_hello("Alice"))
    print(emphasize("Important"))
