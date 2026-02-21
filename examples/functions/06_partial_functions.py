"""functools.partial for creating specialized functions."""

from functools import partial


def power(base, exponent):
    """Raise base to the given exponent."""
    return base ** exponent


def log_message(level, message):
    """Print a log message with a severity level."""
    print(f"[{level}] {message}")


square = partial(power, exponent=2)
cube = partial(power, exponent=3)

info = partial(log_message, "INFO")
error = partial(log_message, "ERROR")


def make_adder(n):
    """Create an adder using partial instead of a closure."""
    return partial(lambda a, b: a + b, n)


if __name__ == "__main__":
    print(f"square(5) = {square(5)}")
    print(f"cube(3) = {cube(3)}")
    info("Server started")
    error("Connection lost")
    add5 = make_adder(5)
    print(f"add5(10) = {add5(10)}")
