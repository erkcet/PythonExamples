"""Basic profiling with cProfile."""

import cProfile
import pstats
import io


def slow_sort(data):
    """An intentionally slow bubble sort."""
    arr = list(data)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def fast_sort(data):
    """Use built-in sorted."""
    return sorted(data)


def profile_function(func, *args):
    """Profile a function and print results."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args)
    profiler.disable()
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumulative")
    stats.print_stats(5)
    print(stream.getvalue())
    return result


if __name__ == "__main__":
    import random
    data = random.sample(range(500), 500)

    print("=== Profiling bubble sort ===")
    profile_function(slow_sort, data)

    print("=== Profiling built-in sort ===")
    profile_function(fast_sort, data)
