"""Priority queue implementation using heapq."""

import heapq


class PriorityQueue:
    """Min-priority queue with push and pop operations."""

    def __init__(self):
        self._heap = []
        self._counter = 0  # tie-breaker for equal priorities

    def push(self, item, priority):
        """Add an item with the given priority (lower = higher priority)."""
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self):
        """Remove and return the highest-priority item."""
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self._heap)[2]

    def peek(self):
        """Return the highest-priority item without removing it."""
        return self._heap[0][2]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("low priority", 10)
    pq.push("high priority", 1)
    pq.push("medium priority", 5)
    while not pq.is_empty():
        print(f"Popped: {pq.pop()}")
