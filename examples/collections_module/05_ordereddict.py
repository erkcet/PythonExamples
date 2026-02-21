"""OrderedDict for insertion-order-preserving dictionaries."""

from collections import OrderedDict


def create_ordered_dict():
    """Create an OrderedDict and demonstrate order preservation."""
    od = OrderedDict()
    od["banana"] = 3
    od["apple"] = 1
    od["cherry"] = 2
    return od


def move_to_end(od, key, last=True):
    """Move a key to the beginning or end of the OrderedDict."""
    od.move_to_end(key, last=last)
    return od


def lru_cache_manual(capacity):
    """Implement a simple LRU cache using OrderedDict."""
    cache = OrderedDict()

    def access(key, value=None):
        if key in cache:
            cache.move_to_end(key)
            return cache[key]
        if value is not None:
            cache[key] = value
            if len(cache) > capacity:
                cache.popitem(last=False)
        return value
    return access, cache


if __name__ == "__main__":
    od = create_ordered_dict()
    print("OrderedDict:", od)

    move_to_end(od, "apple", last=False)
    print("After move 'apple' to front:", od)

    access, cache = lru_cache_manual(3)
    for k, v in [("a", 1), ("b", 2), ("c", 3), ("d", 4)]:
        access(k, v)
    print(f"\nLRU cache (cap=3): {dict(cache)}")

    # Equality comparison (order matters for OrderedDict==OrderedDict)
    od1 = OrderedDict([("a", 1), ("b", 2)])
    od2 = OrderedDict([("b", 2), ("a", 1)])
    print(f"\nod1 == od2 (OrderedDict): {od1 == od2}")
    print(f"dict(od1) == dict(od2):   {dict(od1) == dict(od2)}")
