"""Union-Find (Disjoint Set) data structure."""


class DisjointSet:
    """Disjoint set with path compression and union by rank."""

    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}

    def find(self, x):
        """Find root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        """Merge the sets containing a and b. Return True if merged."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

    def connected(self, a, b):
        """Return True if a and b are in the same set."""
        return self.find(a) == self.find(b)


if __name__ == "__main__":
    ds = DisjointSet(range(6))
    ds.union(0, 1)
    ds.union(2, 3)
    ds.union(1, 3)
    print(f"0 and 3 connected: {ds.connected(0, 3)}")
    print(f"0 and 5 connected: {ds.connected(0, 5)}")
