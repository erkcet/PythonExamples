"""Timeouts with asyncio.wait_for and asyncio.timeout."""

import asyncio


async def slow_operation(seconds):
    """Simulate a slow operation."""
    await asyncio.sleep(seconds)
    return f"Completed after {seconds}s"


async def with_wait_for(timeout):
    """Use asyncio.wait_for for timeout control."""
    try:
        result = await asyncio.wait_for(slow_operation(2.0), timeout=timeout)
        return result
    except asyncio.TimeoutError:
        return f"Timed out after {timeout}s"


async def with_timeout_context(timeout):
    """Use asyncio.timeout context manager (Python 3.11+)."""
    try:
        async with asyncio.timeout(timeout):
            result = await slow_operation(2.0)
            return result
    except asyncio.TimeoutError:
        return f"Timed out after {timeout}s"


async def first_completed():
    """Return result of whichever task finishes first."""
    tasks = [slow_operation(0.3), slow_operation(0.1), slow_operation(0.2)]
    done, pending = await asyncio.wait(
        [asyncio.create_task(t) for t in tasks], return_when=asyncio.FIRST_COMPLETED
    )
    for t in pending:
        t.cancel()
    return done.pop().result()


if __name__ == "__main__":
    print("wait_for (short):", asyncio.run(with_wait_for(0.1)))
    print("timeout ctx:     ", asyncio.run(with_timeout_context(0.1)))
    print("First completed: ", asyncio.run(first_completed()))
