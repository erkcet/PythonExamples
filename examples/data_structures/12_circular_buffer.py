"""Circular buffer (ring buffer) implementation."""


class CircularBuffer:
    """Fixed-size circular buffer that overwrites oldest data."""

    def __init__(self, capacity):
        self._buf = [None] * capacity
        self._capacity = capacity
        self._head = 0   # next write position
        self._size = 0

    def write(self, item):
        """Write an item; overwrites the oldest if full."""
        self._buf[self._head] = item
        self._head = (self._head + 1) % self._capacity
        self._size = min(self._size + 1, self._capacity)

    def read_all(self):
        """Return all items from oldest to newest."""
        if self._size < self._capacity:
            return self._buf[:self._size]
        start = self._head  # oldest element
        return [self._buf[(start + i) % self._capacity] for i in range(self._capacity)]

    def is_full(self):
        """Return True if buffer is at capacity."""
        return self._size == self._capacity

    def __len__(self):
        return self._size


if __name__ == "__main__":
    cb = CircularBuffer(3)
    for v in [1, 2, 3, 4, 5]:
        cb.write(v)
    print(f"Buffer contents: {cb.read_all()}")
    print(f"Full: {cb.is_full()}, Size: {len(cb)}")
