"""Using the @contextmanager decorator from contextlib."""

from contextlib import contextmanager


@contextmanager
def managed_resource(name):
    """A generator-based context manager."""
    print(f"Acquiring {name}")
    resource = {"name": name, "active": True}
    try:
        yield resource
    finally:
        resource["active"] = False
        print(f"Releasing {name}")


@contextmanager
def indented_print(prefix="  "):
    """Context that tracks indented output."""
    items = []
    yield items
    for item in items:
        print(f"{prefix}{item}")


@contextmanager
def error_boundary(label):
    """Catch and log errors within a block."""
    print(f"[{label}] Starting")
    try:
        yield
    except Exception as e:
        print(f"[{label}] Error caught: {e}")
    else:
        print(f"[{label}] Completed successfully")


if __name__ == "__main__":
    with managed_resource("connection") as conn:
        print(f"Using: {conn}")
    print(f"After: {conn}")

    print("\n--- Indented output ---")
    with indented_print(">> ") as items:
        items.extend(["first", "second", "third"])

    print("\n--- Error boundary ---")
    with error_boundary("safe-block"):
        raise RuntimeError("oops")
