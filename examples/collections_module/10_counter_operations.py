"""Counter arithmetic and advanced methods."""

from collections import Counter


def demonstrate_arithmetic():
    """Show Counter addition, subtraction, intersection, union."""
    a = Counter(x=4, y=2, z=1)
    b = Counter(x=1, y=3, w=5)
    return {
        "a + b": a + b,
        "a - b": a - b,
        "a & b (min)": a & b,
        "a | b (max)": a | b,
    }


def positive_only(counter):
    """Keep only elements with positive counts."""
    return +counter


def inventory_check(stock, order):
    """Check if stock can fulfill an order."""
    shortage = order - stock
    return {"can_fulfill": not shortage, "shortage": shortage or "none"}


if __name__ == "__main__":
    print("Counter arithmetic:")
    for op, result in demonstrate_arithmetic().items():
        print(f"  {op}: {dict(result)}")

    mixed = Counter(a=3, b=-1, c=0, d=2)
    print(f"\nMixed: {dict(mixed)}")
    print(f"Positive only: {dict(positive_only(mixed))}")

    stock = Counter(apple=10, banana=5, orange=3)
    order = Counter(apple=3, banana=8, cherry=2)
    print(f"\nInventory check: {inventory_check(stock, order)}")

    # Total count
    c = Counter("mississippi")
    print(f"\n'mississippi' counts: {c}")
    print(f"Total: {c.total()}")
    print(f"Most common 2: {c.most_common(2)}")
