"""Async generators for streaming data."""

import asyncio


async def async_range(start, stop, delay=0.05):
    """Async generator that yields numbers with a delay."""
    for i in range(start, stop):
        await asyncio.sleep(delay)
        yield i


async def async_fibonacci(limit):
    """Async generator for Fibonacci numbers up to a limit."""
    a, b = 0, 1
    while a < limit:
        await asyncio.sleep(0.01)
        yield a
        a, b = b, a + b


async def async_filter(agen, predicate):
    """Filter an async generator with a predicate."""
    async for item in agen:
        if predicate(item):
            yield item


async def collect(agen):
    """Collect all items from an async generator into a list."""
    return [item async for item in agen]


if __name__ == "__main__":
    print("Async range:", asyncio.run(collect(async_range(0, 5))))
    print("Async fib:  ", asyncio.run(collect(async_fibonacci(50))))
    evens = async_filter(async_range(0, 10), lambda x: x % 2 == 0)
    print("Even only:  ", asyncio.run(collect(evens)))
