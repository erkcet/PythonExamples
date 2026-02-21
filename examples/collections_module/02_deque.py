"""deque operations for efficient double-ended queue usage."""

from collections import deque


def demonstrate_basic_ops():
    """Show basic deque operations: append, pop from both ends."""
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    left = dq.popleft()
    right = dq.pop()
    return {"deque": list(dq), "popped_left": left, "popped_right": right}


def sliding_window(iterable, size):
    """Implement a sliding window using a bounded deque."""
    window = deque(maxlen=size)
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield list(window)


def rotate_deque(items, n):
    """Rotate a deque n steps to the right."""
    dq = deque(items)
    dq.rotate(n)
    return list(dq)


if __name__ == "__main__":
    print("Basic ops:", demonstrate_basic_ops())

    data = [1, 2, 3, 4, 5, 6, 7]
    print("\nSliding window (size 3):")
    for window in sliding_window(data, 3):
        print(f"  {window}")

    print(f"\nRotate [1,2,3,4,5] by  2: {rotate_deque([1,2,3,4,5], 2)}")
    print(f"Rotate [1,2,3,4,5] by -1: {rotate_deque([1,2,3,4,5], -1)}")

    dq = deque([1, 2, 3, 2, 1], maxlen=5)
    print(f"\nCount of 2: {dq.count(2)}, maxlen: {dq.maxlen}")
