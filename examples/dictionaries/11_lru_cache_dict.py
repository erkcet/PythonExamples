"""Implementing an LRU cache using OrderedDict."""

from collections import OrderedDict


class LRUCache:
    """Least Recently Used cache with fixed capacity."""

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """Get value and mark as recently used."""
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """Insert or update; evict LRU if at capacity."""
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def __repr__(self):
        return f"LRUCache({dict(self.cache)})"


if __name__ == "__main__":
    cache = LRUCache(3)
    for k, v in [("a", 1), ("b", 2), ("c", 3)]:
        cache.put(k, v)
    print(f"Full: {cache}")
    print(f"Get 'a': {cache.get('a')}")
    cache.put("d", 4)  # evicts 'b' (LRU)
    print(f"After adding 'd': {cache}")
    print(f"Get 'b': {cache.get('b')}")  # -1, evicted
