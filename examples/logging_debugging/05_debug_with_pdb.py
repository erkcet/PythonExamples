"""Debugging techniques demonstration (print-based, no interactive pdb)."""

import inspect


def debug_print(label, value):
    """Simple debug print with caller info."""
    frame = inspect.stack()[1]
    location = f"{frame.filename}:{frame.lineno}"
    print(f"[DEBUG {location}] {label} = {value!r}")


def trace_calls(func):
    """Decorator that traces function calls and returns."""
    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args] +
                            [f"{k}={v!r}" for k, v in kwargs.items()])
        print(f"CALL {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"  => {result!r}")
        return result
    return wrapper


@trace_calls
def fibonacci(n):
    """Compute fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def inspect_variables():
    """Show how to inspect local variables."""
    x = 42
    name = "debug"
    items = [1, 2, 3]
    local_vars = {k: v for k, v in locals().items()}
    print(f"Local variables: {local_vars}")


if __name__ == "__main__":
    debug_print("test_value", {"key": [1, 2, 3]})
    print("\n--- Traced fibonacci(4) ---")
    fibonacci(4)
    print("\n--- Variable inspection ---")
    inspect_variables()
