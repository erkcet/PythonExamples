"""Resource pool context manager."""

import queue
from contextlib import contextmanager


class ResourcePool:
    """A pool of reusable resources."""

    def __init__(self, factory, size=3):
        self.pool = queue.Queue(maxsize=size)
        for i in range(size):
            self.pool.put(factory(i))
        self.size = size

    @contextmanager
    def acquire(self):
        """Acquire a resource from the pool."""
        resource = self.pool.get()
        print(f"  Acquired: {resource}")
        try:
            yield resource
        finally:
            self.pool.put(resource)
            print(f"  Released: {resource}")

    @property
    def available(self):
        return self.pool.qsize()


def make_connection(id_):
    """Factory for simulated connections."""
    return f"Connection-{id_}"


if __name__ == "__main__":
    pool = ResourcePool(make_connection, size=3)
    print(f"Available: {pool.available}")

    with pool.acquire() as conn1:
        print(f"Using {conn1}, available: {pool.available}")
        with pool.acquire() as conn2:
            print(f"Using {conn1} and {conn2}, available: {pool.available}")
        print(f"Released conn2, available: {pool.available}")
    print(f"All released, available: {pool.available}")
