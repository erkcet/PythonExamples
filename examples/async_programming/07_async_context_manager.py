"""Async context managers for resource management."""

import asyncio


class AsyncResource:
    """An async context manager for a simulated resource."""

    def __init__(self, name):
        self.name = name

    async def __aenter__(self):
        print(f"  Acquiring {self.name}...")
        await asyncio.sleep(0.05)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"  Releasing {self.name}...")
        await asyncio.sleep(0.05)
        return False

    async def operate(self):
        return f"{self.name}: operation complete"


class AsyncDBConnection:
    """Simulated async database connection."""

    def __init__(self, dsn):
        self.dsn = dsn
        self.connected = False

    async def __aenter__(self):
        self.connected = True
        await asyncio.sleep(0.01)
        return self

    async def __aexit__(self, *args):
        self.connected = False
        await asyncio.sleep(0.01)

    async def query(self, sql):
        return f"Result of '{sql}' from {self.dsn}"


async def main():
    async with AsyncResource("Lock-A") as res:
        print(f"  {await res.operate()}")
    async with AsyncDBConnection("sqlite://test.db") as db:
        print(f"  {await db.query('SELECT 1')}")


if __name__ == "__main__":
    asyncio.run(main())
