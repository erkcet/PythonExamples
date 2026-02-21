"""Nested and multiple context managers."""

from contextlib import contextmanager, ExitStack


@contextmanager
def tag(name):
    """Print opening and closing tags."""
    print(f"<{name}>")
    yield name
    print(f"</{name}>")


def nested_contexts():
    """Use multiple context managers with single 'with'."""
    with tag("html") as h, tag("body") as b, tag("p") as p:
        print(f"  Content inside {h}/{b}/{p}")


def dynamic_contexts(names):
    """Use ExitStack for a dynamic number of contexts."""
    with ExitStack() as stack:
        tags = [stack.enter_context(tag(n)) for n in names]
        print(f"  Active tags: {tags}")


def exitstack_callbacks():
    """Register cleanup callbacks with ExitStack."""
    with ExitStack() as stack:
        stack.callback(print, "Cleanup 1")
        stack.callback(print, "Cleanup 2")
        print("Inside the block")
    print("After block")


if __name__ == "__main__":
    print("=== Nested ===")
    nested_contexts()
    print("\n=== Dynamic ===")
    dynamic_contexts(["div", "span", "em"])
    print("\n=== Callbacks ===")
    exitstack_callbacks()
