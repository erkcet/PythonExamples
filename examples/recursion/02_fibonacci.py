"""Fibonacci Sequence with Memoization.

Computes Fibonacci numbers using naive recursion and optimized
memoized recursion. Demonstrates dramatic performance difference.
"""

from functools import lru_cache
import time


def fib_naive(n: int) -> int:
    """Compute nth Fibonacci number (naive, exponential time)."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Compute nth Fibonacci number with memoization. O(n) time."""
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_manual_memo(n: int, memo: dict = None) -> int:
    """Compute nth Fibonacci with manual memoization dict."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_manual_memo(n - 1, memo) + fib_manual_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    start = time.time()
    print(f"Naive fib(30) = {fib_naive(30)}  ({time.time()-start:.3f}s)")
    start = time.time()
    print(f"Memo  fib(30) = {fib_memo(30)}  ({time.time()-start:.6f}s)")
    print(f"Memo  fib(100) = {fib_memo(100)}")
