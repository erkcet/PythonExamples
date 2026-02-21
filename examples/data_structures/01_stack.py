"""Stack implementation using a Python list."""


class Stack:
    """LIFO stack backed by a list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push an item onto the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    s = Stack()
    for val in [10, 20, 30]:
        s.push(val)
    print(f"Top: {s.peek()}, Size: {len(s)}")
    while not s.is_empty():
        print(f"Popped: {s.pop()}")
