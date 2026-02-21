"""Queue implementation using collections.deque."""

from collections import deque


class Queue:
    """FIFO queue backed by a deque for O(1) operations."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the back."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    q = Queue()
    for val in [1, 2, 3]:
        q.enqueue(val)
    print(f"Front: {q.peek()}, Size: {len(q)}")
    while not q.is_empty():
        print(f"Dequeued: {q.dequeue()}")
