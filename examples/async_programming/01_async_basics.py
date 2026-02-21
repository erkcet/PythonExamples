"""Basic async/await syntax and coroutine fundamentals."""

import asyncio


async def greet(name, delay=1):
    """Async greeting with a simulated delay."""
    await asyncio.sleep(delay)
    return f"Hello, {name}!"


async def compute(x, y):
    """Simulate an async computation."""
    await asyncio.sleep(0.1)
    return x + y


async def chain_operations():
    """Chain multiple async operations sequentially."""
    greeting = await greet("World", 0.1)
    result = await compute(3, 4)
    return f"{greeting} 3+4={result}"


if __name__ == "__main__":
    result = asyncio.run(greet("Python", 0.1))
    print(result)
    result = asyncio.run(chain_operations())
    print(result)
