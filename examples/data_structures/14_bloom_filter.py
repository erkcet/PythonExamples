"""Simple Bloom filter implementation."""

import hashlib


class BloomFilter:
    """Probabilistic set membership using multiple hash functions."""

    def __init__(self, size=1000, num_hashes=3):
        self._size = size
        self._num_hashes = num_hashes
        self._bits = [False] * size

    def _hashes(self, item):
        """Generate hash indices for an item."""
        indices = []
        for i in range(self._num_hashes):
            h = hashlib.md5(f"{item}:{i}".encode()).hexdigest()
            indices.append(int(h, 16) % self._size)
        return indices

    def add(self, item):
        """Add an item to the filter."""
        for idx in self._hashes(item):
            self._bits[idx] = True

    def might_contain(self, item):
        """Return True if item *might* be in the set (false positives possible)."""
        return all(self._bits[idx] for idx in self._hashes(item))


if __name__ == "__main__":
    bf = BloomFilter(size=500, num_hashes=3)
    for word in ["hello", "world", "python"]:
        bf.add(word)
    print(f"'hello'  in filter: {bf.might_contain('hello')}")
    print(f"'world'  in filter: {bf.might_contain('world')}")
    print(f"'java'   in filter: {bf.might_contain('java')}")
