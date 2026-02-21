"""Singleton pattern: ensure a class has only one instance."""


class Singleton:
    """A class that allows only one instance to exist."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if value is not None:
            self.value = value


def demonstrate_singleton():
    """Show that two instances are actually the same object."""
    a = Singleton("first")
    b = Singleton("second")
    print(f"a.value = {a.value}")
    print(f"b.value = {b.value}")
    print(f"a is b: {a is b}")


if __name__ == "__main__":
    demonstrate_singleton()
