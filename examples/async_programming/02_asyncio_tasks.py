"""Creating and running asyncio tasks."""

import asyncio


async def worker(name, duration):
    """Simulate a worker that takes some time."""
    print(f"  {name} started")
    await asyncio.sleep(duration)
    print(f"  {name} finished after {duration}s")
    return f"{name}: done"


async def run_tasks():
    """Create and manage multiple tasks."""
    task1 = asyncio.create_task(worker("Task-A", 0.3))
    task2 = asyncio.create_task(worker("Task-B", 0.1))
    task3 = asyncio.create_task(worker("Task-C", 0.2))
    results = []
    for task in [task1, task2, task3]:
        results.append(await task)
    return results


async def task_with_cancel():
    """Demonstrate task cancellation."""
    async def long_running():
        await asyncio.sleep(10)

    task = asyncio.create_task(long_running())
    await asyncio.sleep(0.1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("  Task was cancelled successfully")


if __name__ == "__main__":
    print("Running tasks concurrently:")
    results = asyncio.run(run_tasks())
    print(f"Results: {results}")
    print("\nCancellation demo:")
    asyncio.run(task_with_cancel())
