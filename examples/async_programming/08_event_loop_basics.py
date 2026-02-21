"""Event loop fundamentals and scheduling."""

import asyncio
import time


async def scheduled_callback(delay, message):
    """Coroutine that runs after a delay."""
    await asyncio.sleep(delay)
    print(f"  [{time.perf_counter():.2f}] {message}")


async def demonstrate_scheduling():
    """Show different ways to schedule work on the event loop."""
    loop = asyncio.get_running_loop()
    print(f"  Loop running: {loop.is_running()}")
    print(f"  Loop time: {loop.time():.4f}")
    tasks = [
        asyncio.create_task(scheduled_callback(0.1, "First")),
        asyncio.create_task(scheduled_callback(0.05, "Second (faster)")),
        asyncio.create_task(scheduled_callback(0.15, "Third")),
    ]
    await asyncio.gather(*tasks)


async def run_in_executor_demo():
    """Run blocking code in an executor."""
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, time.strftime, "%H:%M:%S")
    return f"Time from executor: {result}"


if __name__ == "__main__":
    print("Scheduling demo:")
    asyncio.run(demonstrate_scheduling())
    print("\nExecutor demo:")
    print(f"  {asyncio.run(run_in_executor_demo())}")
