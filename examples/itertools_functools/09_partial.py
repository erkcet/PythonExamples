"""functools.partial for creating specialized function variants."""

from functools import partial


def power(base, exponent):
    """Raise base to the given exponent."""
    return base ** exponent


def log_message(level, component, message):
    """Format a log message with level and component."""
    return f"[{level}] {component}: {message}"


# Create specialized functions using partial
square = partial(power, exponent=2)
cube = partial(power, exponent=3)
info_log = partial(log_message, "INFO")
error_log = partial(log_message, "ERROR")
db_error = partial(log_message, "ERROR", "DATABASE")


def make_multiplier(factor):
    """Create a multiplier function using partial."""
    return partial(lambda f, x: f * x, factor)


if __name__ == "__main__":
    print(f"square(5): {square(5)}")
    print(f"cube(3):   {cube(3)}")

    print(f"\n{info_log('AUTH', 'User logged in')}")
    print(f"{error_log('DB', 'Connection lost')}")
    print(f"{db_error('Timeout after 30s')}")

    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"\ndouble(7): {double(7)}")
    print(f"triple(7): {triple(7)}")

    # partial with built-ins
    to_binary = partial(int, base=2)
    print(f"\nBinary '1010' -> {to_binary('1010')}")

    # Inspect partial attributes
    print(f"\nsquare.func: {square.func.__name__}")
    print(f"square.keywords: {square.keywords}")
