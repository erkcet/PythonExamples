"""Timing code with timeit and time.perf_counter."""

import timeit
import time


def time_with_perf_counter(func, *args, runs=5):
    """Time a function using perf_counter."""
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        func(*args)
        times.append(time.perf_counter() - start)
    avg = sum(times) / len(times)
    print(f"  {func.__name__}: avg={avg:.6f}s min={min(times):.6f}s ({runs} runs)")


def list_comp(n):
    """Build list with comprehension."""
    return [i * i for i in range(n)]


def map_func(n):
    """Build list with map."""
    return list(map(lambda i: i * i, range(n)))


def for_loop(n):
    """Build list with for loop."""
    result = []
    for i in range(n):
        result.append(i * i)
    return result


def use_timeit():
    """Use timeit module for micro-benchmarks."""
    tests = {
        "list comp": "[i*i for i in range(1000)]",
        "map+lambda": "list(map(lambda i: i*i, range(1000)))",
        "for loop": "r=[]\nfor i in range(1000): r.append(i*i)",
    }
    for label, stmt in tests.items():
        t = timeit.timeit(stmt, number=1000)
        print(f"  {label:15s}: {t:.4f}s (1000 iterations)")


if __name__ == "__main__":
    n = 10_000
    print("=== perf_counter timing ===")
    time_with_perf_counter(list_comp, n)
    time_with_perf_counter(map_func, n)
    time_with_perf_counter(for_loop, n)
    print("\n=== timeit micro-benchmarks ===")
    use_timeit()
