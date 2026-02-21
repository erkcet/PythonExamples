"""Using assert statements for simple inline testing."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0


def run_assertions():
    """Demonstrate assert statements with helpful messages."""
    assert add(2, 3) == 5, "2 + 3 should equal 5"
    assert add(-1, 1) == 0, "Negative plus positive should work"
    assert is_even(4), "4 should be even"
    assert not is_even(7), "7 should not be even"
    assert isinstance(add(1.0, 2), float), "Float input gives float output"
    print("All assertions passed!")


if __name__ == "__main__":
    run_assertions()
