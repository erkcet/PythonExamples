"""Redirect stdout and stderr using context managers."""

import io
import sys
from contextlib import redirect_stdout, redirect_stderr


def capture_stdout(func, *args):
    """Capture stdout from a function call."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        result = func(*args)
    return result, buffer.getvalue()


def capture_stderr(func, *args):
    """Capture stderr from a function call."""
    buffer = io.StringIO()
    with redirect_stderr(buffer):
        result = func(*args)
    return result, buffer.getvalue()


def noisy_function(n):
    """A function that prints while computing."""
    print(f"Computing sum of 1..{n}")
    result = sum(range(1, n + 1))
    print(f"Done!")
    return result


def warning_function():
    """A function that writes to stderr."""
    print("Warning: low disk space", file=sys.stderr)
    return "ok"


if __name__ == "__main__":
    result, output = capture_stdout(noisy_function, 100)
    print(f"Result: {result}")
    print(f"Captured output: {output!r}")

    print("-" * 40)
    result, errors = capture_stderr(warning_function)
    print(f"Result: {result}")
    print(f"Captured stderr: {errors!r}")
