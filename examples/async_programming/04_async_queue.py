"""Async producer-consumer pattern with asyncio.Queue."""

import asyncio
import random


async def producer(queue, name, count):
    """Produce items and put them on the queue."""
    for i in range(count):
        item = f"{name}-item-{i}"
        await queue.put(item)
        await asyncio.sleep(random.uniform(0.01, 0.05))
    print(f"  {name} finished producing {count} items")


async def consumer(queue, name):
    """Consume items from the queue until sentinel."""
    consumed = 0
    while True:
        item = await queue.get()
        if item is None:
            break
        consumed += 1
        queue.task_done()
    print(f"  {name} consumed {consumed} items")


async def main():
    """Run producer-consumer pipeline."""
    queue = asyncio.Queue(maxsize=5)
    producers = [
        asyncio.create_task(producer(queue, f"P{i}", 4)) for i in range(2)
    ]
    consumers = [
        asyncio.create_task(consumer(queue, f"C{i}")) for i in range(2)
    ]
    await asyncio.gather(*producers)
    for _ in consumers:
        await queue.put(None)
    await asyncio.gather(*consumers)


if __name__ == "__main__":
    print("Producer-Consumer with asyncio.Queue:")
    asyncio.run(main())
