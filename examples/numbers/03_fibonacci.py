"""Generate Fibonacci sequence."""


def fibonacci_iterative(n: int) -> list[int]:
    """Return the first n Fibonacci numbers iteratively."""
    if n <= 0:
        return []
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]


def fibonacci_recursive(n: int) -> int:
    """Return the nth Fibonacci number recursively."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_generator(limit: int):
    """Yield Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("First 15:", fibonacci_iterative(15))
    print("Recursive F(10):", fibonacci_recursive(10))
    print("Up to 100:", list(fibonacci_generator(100)))
