"""LRU (Least Recently Used) cache from scratch."""

from collections import OrderedDict


class LRUCache:
    """LRU cache using OrderedDict."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """Get value by key, returning None if not found."""
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """Insert or update a key-value pair."""
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def __repr__(self):
        return f"LRUCache({dict(self.cache)})"

    def __len__(self):
        return len(self.cache)


if __name__ == "__main__":
    cache = LRUCache(3)
    for k, v in [("a", 1), ("b", 2), ("c", 3)]:
        cache.put(k, v)
    print(f"Full cache: {cache}")
    print(f"Get 'a': {cache.get('a')}")
    cache.put("d", 4)  # Evicts 'b' (least recently used)
    print(f"After adding 'd': {cache}")
    print(f"Get 'b': {cache.get('b')}")  # None, was evicted
    cache.put("e", 5)  # Evicts 'c'
    print(f"After adding 'e': {cache}")
