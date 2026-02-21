"""Using asyncio.gather for concurrent task execution."""

import asyncio
import time


async def fetch_data(source, delay):
    """Simulate fetching data from a source."""
    await asyncio.sleep(delay)
    return {"source": source, "data": f"result from {source}"}


async def gather_all():
    """Run multiple coroutines concurrently with gather."""
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch_data("api-1", 0.3),
        fetch_data("api-2", 0.2),
        fetch_data("api-3", 0.1),
    )
    elapsed = time.perf_counter() - start
    return results, elapsed


async def gather_with_errors():
    """Handle errors in gathered tasks."""
    async def failing_task():
        raise ValueError("Something went wrong")

    results = await asyncio.gather(
        fetch_data("ok-source", 0.1),
        failing_task(),
        return_exceptions=True,
    )
    return results


if __name__ == "__main__":
    results, elapsed = asyncio.run(gather_all())
    print(f"All results ({elapsed:.2f}s):")
    for r in results:
        print(f"  {r}")
    print("\nWith error handling:")
    for r in asyncio.run(gather_with_errors()):
        print(f"  {r}")
