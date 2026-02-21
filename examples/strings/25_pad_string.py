"""Demonstrate various string padding techniques."""


def pad_left(s, width, fill=' '):
    """Pad string on the left to reach the desired width."""
    return (fill * (width - len(s))) + s if len(s) < width else s


def pad_right(s, width, fill=' '):
    """Pad string on the right to reach the desired width."""
    return s + (fill * (width - len(s))) if len(s) < width else s


if __name__ == "__main__":
    items = ["42", "7", "256", "1000"]
    print("Left-padded with zeros (width=6):")
    for item in items:
        print(f"  '{pad_left(item, 6, '0')}'")
    print("Right-padded with dots (width=10):")
    for item in items:
        print(f"  '{pad_right(item, 10, '.')}'")
    print("Built-in methods:")
    for item in items:
        print(f"  rjust: '{item.rjust(6, '0')}'  ljust: '{item.ljust(10, '.')}'")
