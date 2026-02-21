"""Hash table implementation using separate chaining."""


class HashTable:
    """Simple hash table with separate chaining."""

    def __init__(self, capacity=8):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _index(self, key):
        return hash(key) % len(self._buckets)

    def put(self, key, value):
        """Insert or update a key-value pair."""
        idx = self._index(key)
        for i, (k, _) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx][i] = (key, value)
                return
        self._buckets[idx].append((key, value))
        self._size += 1

    def get(self, key, default=None):
        """Retrieve value by key."""
        for k, v in self._buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def delete(self, key):
        """Remove a key-value pair."""
        idx = self._index(key)
        for i, (k, _) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx].pop(i)
                self._size -= 1
                return True
        return False

    def __len__(self):
        return self._size


if __name__ == "__main__":
    ht = HashTable()
    ht.put("apple", 3)
    ht.put("banana", 5)
    print(f"apple -> {ht.get('apple')}, size={len(ht)}")
    ht.delete("apple")
    print(f"apple after delete -> {ht.get('apple')}")
