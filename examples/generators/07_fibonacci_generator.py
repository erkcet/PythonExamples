"""Fibonacci sequence as a generator."""


def fibonacci():
    """Yield an infinite Fibonacci sequence: 0, 1, 1, 2, 3, 5, ..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_up_to(limit):
    """Yield Fibonacci numbers that do not exceed limit."""
    for n in fibonacci():
        if n > limit:
            return
        yield n


def nth_fibonacci(n):
    """Return the nth Fibonacci number (0-indexed)."""
    gen = fibonacci()
    for _ in range(n):
        next(gen)
    return next(gen)


if __name__ == "__main__":
    import itertools

    first_15 = list(itertools.islice(fibonacci(), 15))
    print(f"First 15: {first_15}")

    up_to_100 = list(fibonacci_up_to(100))
    print(f"Up to 100: {up_to_100}")

    print(f"10th Fibonacci: {nth_fibonacci(10)}")
    print(f"20th Fibonacci: {nth_fibonacci(20)}")
