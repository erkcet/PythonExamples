"""Abstract base classes from collections.abc."""

from collections.abc import Mapping, Sequence, Iterable, Iterator


class SquareSequence(Sequence):
    """A virtual sequence of squares: 0, 1, 4, 9, 16, ..."""

    def __init__(self, length):
        self._length = length

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("index out of range")
        return index ** 2

    def __len__(self):
        return self._length


class FibIterator(Iterator):
    """An iterator that yields Fibonacci numbers."""

    def __init__(self, limit):
        self._a, self._b = 0, 1
        self._limit = limit
        self._count = 0

    def __next__(self):
        if self._count >= self._limit:
            raise StopIteration
        self._count += 1
        result = self._a
        self._a, self._b = self._b, self._a + self._b
        return result


if __name__ == "__main__":
    sq = SquareSequence(6)
    print("Squares:", list(sq))
    print("sq[3]:", sq[3], " | len:", len(sq))

    fib = FibIterator(10)
    print("\nFibonacci:", list(fib))

    # isinstance checks with ABCs
    print(f"\ndict is Mapping: {isinstance({}, Mapping)}")
    print(f"list is Sequence: {isinstance([], Sequence)}")
    print(f"str is Iterable: {isinstance('hi', Iterable)}")
    print(f"SquareSequence is Sequence: {isinstance(sq, Sequence)}")
