"""Basic context manager using __enter__ and __exit__."""


class ManagedResource:
    """A resource that must be opened and closed."""

    def __init__(self, name):
        self.name = name
        self.is_open = False

    def __enter__(self):
        self.is_open = True
        print(f"[{self.name}] Resource opened")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_open = False
        print(f"[{self.name}] Resource closed")
        if exc_type is not None:
            print(f"[{self.name}] Exception caught: {exc_val}")
        return False  # Don't suppress exceptions

    def do_work(self):
        """Perform work with the resource."""
        if not self.is_open:
            raise RuntimeError("Resource is not open")
        print(f"[{self.name}] Working...")
        return "done"


if __name__ == "__main__":
    with ManagedResource("DB") as resource:
        result = resource.do_work()
        print(f"Result: {result}")

    print(f"After with: is_open={resource.is_open}")

    print("\n--- With exception ---")
    try:
        with ManagedResource("Net") as r:
            raise ValueError("Something went wrong")
    except ValueError:
        print("Exception propagated as expected")
