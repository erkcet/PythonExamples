"""Min-heap and max-heap using heapq."""

import heapq


def heapsort(iterable):
    """Return a sorted list using heap operations."""
    h = list(iterable)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


class MaxHeap:
    """Max-heap wrapper around heapq (which is a min-heap)."""

    def __init__(self):
        self._heap = []

    def push(self, val):
        """Push a value onto the max-heap."""
        heapq.heappush(self._heap, -val)

    def pop(self):
        """Pop and return the maximum value."""
        return -heapq.heappop(self._heap)

    def peek(self):
        """Return the maximum value without removing it."""
        return -self._heap[0]

    def __len__(self):
        return len(self._heap)


if __name__ == "__main__":
    data = [4, 1, 7, 3, 8, 5]
    print(f"Heapsort: {heapsort(data)}")
    mh = MaxHeap()
    for v in data:
        mh.push(v)
    print(f"Max-heap peek: {mh.peek()}")
    print(f"Max-heap pops: {[mh.pop() for _ in range(len(mh))]}")
