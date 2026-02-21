"""LRU Cache implementation using OrderedDict."""

from collections import OrderedDict


class LRUCache:
    """Least-Recently-Used cache with a fixed capacity."""

    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key):
        """Return value for key and mark it as recently used, or -1."""
        if key not in self._cache:
            return -1
        self._cache.move_to_end(key)
        return self._cache[key]

    def put(self, key, value):
        """Insert or update key-value and evict LRU if over capacity."""
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)

    def __repr__(self):
        return f"LRUCache({dict(self._cache)})"


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(cache)
    cache.get("a")          # 'a' is now most recent
    cache.put("d", 4)       # evicts 'b'
    print(f"After eviction: {cache}")
    print(f"get('b'): {cache.get('b')}")
