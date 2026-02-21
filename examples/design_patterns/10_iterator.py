"""Iterator pattern: traverse a collection without exposing internals."""


class Countdown:
    """An iterable that counts down from a start number to 1."""

    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        """Return a fresh iterator each time."""
        return CountdownIterator(self.start)


class CountdownIterator:
    """Iterator that yields numbers in descending order."""

    def __init__(self, current: int):
        self._current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self._current <= 0:
            raise StopIteration
        value = self._current
        self._current -= 1
        return value


def demonstrate_iterator():
    """Show using a custom iterator in a for loop."""
    countdown = Countdown(5)
    print("First pass: ", list(countdown))
    print("Second pass:", list(countdown))


if __name__ == "__main__":
    demonstrate_iterator()
