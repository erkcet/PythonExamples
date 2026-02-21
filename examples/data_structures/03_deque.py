"""Deque (double-ended queue) implementation using a list."""


class Deque:
    """Double-ended queue supporting O(1) ops at both ends (amortized)."""

    def __init__(self):
        self._items = []

    def push_front(self, item):
        """Add item to the front."""
        self._items.insert(0, item)

    def push_back(self, item):
        """Add item to the back."""
        self._items.append(item)

    def pop_front(self):
        """Remove and return the front item."""
        if not self._items:
            raise IndexError("pop from empty deque")
        return self._items.pop(0)

    def pop_back(self):
        """Remove and return the back item."""
        if not self._items:
            raise IndexError("pop from empty deque")
        return self._items.pop()

    def is_empty(self):
        """Return True if empty."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Deque({self._items})"


if __name__ == "__main__":
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    d.push_front(0)
    print(d)
    print(f"Pop front: {d.pop_front()}, Pop back: {d.pop_back()}")
