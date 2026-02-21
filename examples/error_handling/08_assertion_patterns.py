"""Assert and defensive programming patterns."""


def calculate_discount(price, percent):
    """Calculate discounted price with precondition checks."""
    assert isinstance(price, (int, float)), f"price must be numeric, got {type(price)}"
    assert 0 <= percent <= 100, f"percent must be 0-100, got {percent}"
    return price * (1 - percent / 100)


def process_batch(items):
    """Process a batch ensuring invariants."""
    assert len(items) > 0, "Batch must not be empty"
    results = [item.upper() for item in items]
    assert len(results) == len(items), "Output count must match input"
    return results


def safe_divide(a, b):
    """Divide using defensive checks instead of assertions."""
    if not isinstance(b, (int, float)):
        raise TypeError(f"Divisor must be numeric, got {type(b)}")
    if b == 0:
        raise ValueError("Divisor must not be zero")
    return a / b


if __name__ == "__main__":
    print(f"20% off $50: ${calculate_discount(50, 20):.2f}")
    print(f"Batch: {process_batch(['hello', 'world'])}")
    print(f"10 / 3 = {safe_divide(10, 3):.4f}")

    try:
        calculate_discount(50, 150)
    except AssertionError as e:
        print(f"Assertion caught: {e}")

    try:
        safe_divide(10, 0)
    except ValueError as e:
        print(f"ValueError caught: {e}")
