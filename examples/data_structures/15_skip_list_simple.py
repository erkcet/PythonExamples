"""Simplified skip list concept demonstration."""

import random


class SkipNode:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList:
    """A simplified skip list supporting insert and search."""

    def __init__(self, max_level=4, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(-1, max_level)
        self.level = 0

    def _random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key):
        """Insert a key into the skip list."""
        update = [self.header] * (self.max_level + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        lvl = self._random_level()
        if lvl > self.level:
            self.level = lvl
        node = SkipNode(key, lvl)
        for i in range(lvl + 1):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node

    def search(self, key):
        """Return True if key exists in the skip list."""
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.key == key


if __name__ == "__main__":
    sl = SkipList()
    for v in [3, 6, 7, 9, 12, 19, 25]:
        sl.insert(v)
    print(f"Search 7:  {sl.search(7)}")
    print(f"Search 10: {sl.search(10)}")
