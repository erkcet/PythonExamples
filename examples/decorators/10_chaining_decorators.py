"""Stacking multiple decorators on a single function."""

from functools import wraps


def bold(func):
    """Wrap result in <b> tags."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def italic(func):
    """Wrap result in <i> tags."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


def uppercase(func):
    """Convert result to uppercase."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@bold
@italic
@uppercase
def greet(name):
    """Greet someone with styled text."""
    return f"hello, {name}"


@italic
@bold
def whisper(text):
    """Whisper styled text (different order)."""
    return text


if __name__ == "__main__":
    # Decorators apply bottom-up: uppercase -> italic -> bold
    print(greet("Alice"))
    print(whisper("secret"))
    print(f"Function name preserved: {greet.__name__}")
