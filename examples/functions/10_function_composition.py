"""Composing functions to build pipelines."""

from functools import reduce


def compose(*funcs):
    """Compose functions right-to-left: compose(f, g)(x) == f(g(x))."""
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed


def pipe(*funcs):
    """Pipe functions left-to-right: pipe(f, g)(x) == g(f(x))."""
    return reduce(lambda f, g: lambda x: g(f(x)), funcs)


def add_one(x):
    """Add one."""
    return x + 1


def double(x):
    """Double the value."""
    return x * 2


def to_string(x):
    """Convert to string with label."""
    return f"Result: {x}"


if __name__ == "__main__":
    transform = compose(to_string, double, add_one)
    print(transform(5))  # Result: 12

    pipeline = pipe(add_one, double, to_string)
    print(pipeline(5))  # Result: 12
