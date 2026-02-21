"""OrderedDict usage and comparison with regular dict."""

from collections import OrderedDict


def lru_order_example():
    """Simulate LRU access order with move_to_end."""
    od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    od.move_to_end("a")  # accessed "a", move to end
    od.move_to_end("b")  # accessed "b", move to end
    return od


def fifo_pop():
    """Remove items in insertion order (FIFO)."""
    od = OrderedDict([("first", 1), ("second", 2), ("third", 3)])
    removed = od.popitem(last=False)  # pop from front
    return removed, od


def reversed_iteration():
    """Iterate in reverse insertion order."""
    od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    return list(reversed(od))


def equality_comparison():
    """OrderedDict considers order in equality; dict does not."""
    od1 = OrderedDict([("a", 1), ("b", 2)])
    od2 = OrderedDict([("b", 2), ("a", 1)])
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 2, "a": 1}
    return od1 == od2, d1 == d2


if __name__ == "__main__":
    print(f"LRU order: {lru_order_example()}")
    removed, remaining = fifo_pop()
    print(f"FIFO pop: removed={removed}, remaining={remaining}")
    print(f"Reversed keys: {reversed_iteration()}")
    od_eq, d_eq = equality_comparison()
    print(f"OrderedDict order matters: {od_eq}, Dict ignores: {d_eq}")
