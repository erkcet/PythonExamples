import asyncio

async def worker(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    results = await asyncio.gather(worker("A", 0.1), worker("B", 0.2))
    print(results)

asyncio.run(main())
