"""UserList for creating custom list subclasses."""

from collections import UserList


class SortedList(UserList):
    """A list that maintains sorted order on insertion."""

    def append(self, item):
        super().append(item)
        self.data.sort()

    def extend(self, items):
        super().extend(items)
        self.data.sort()


class BoundedList(UserList):
    """A list with a maximum capacity."""

    def __init__(self, maxlen, initlist=None):
        super().__init__(initlist)
        self._maxlen = maxlen
        self.data = self.data[:maxlen]

    def append(self, item):
        if len(self.data) >= self._maxlen:
            raise OverflowError(f"List is full (max {self._maxlen})")
        super().append(item)


if __name__ == "__main__":
    sl = SortedList([5, 2, 8])
    print("SortedList:", sl)
    sl.append(1)
    sl.append(6)
    print("After appending 1, 6:", sl)
    sl.extend([3, 9])
    print("After extend [3,9]:", sl)

    bl = BoundedList(3)
    bl.append("a")
    bl.append("b")
    bl.append("c")
    print(f"\nBoundedList: {bl}")
    try:
        bl.append("d")
    except OverflowError as e:
        print(f"Overflow: {e}")
