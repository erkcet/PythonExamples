"""Basic try/except/else/finally demonstration."""


def divide(a, b):
    """Divide a by b with full error handling."""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero")
        return None
    except TypeError as e:
        print(f"Error: Invalid types - {e}")
        return None
    else:
        print(f"{a} / {b} = {result}")
        return result
    finally:
        print("Division operation complete")


def safe_int(value):
    """Safely convert a value to int."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


if __name__ == "__main__":
    divide(10, 3)
    divide(10, 0)
    divide("a", 2)
    print(f"safe_int('42') = {safe_int('42')}")
    print(f"safe_int('abc') = {safe_int('abc')}")
