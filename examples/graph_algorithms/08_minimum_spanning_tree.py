"""Minimum spanning tree using Kruskal's algorithm."""


def find(parent, x):
    """Find root with path compression."""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, a, b):
    """Union by rank. Return True if merged."""
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return True


def kruskal(nodes, edges):
    """Return MST edges and total weight.

    Args:
        nodes: iterable of node labels.
        edges: list of (weight, u, v).
    """
    parent = {n: n for n in nodes}
    rank = {n: 0 for n in nodes}
    mst, total = [], 0
    for w, u, v in sorted(edges):
        if union(parent, rank, u, v):
            mst.append((u, v, w))
            total += w
    return mst, total


if __name__ == "__main__":
    edges = [(1, "A", "B"), (3, "A", "C"), (2, "B", "C"), (4, "C", "D")]
    mst, cost = kruskal("ABCD", edges)
    print(f"MST edges: {mst}")
    print(f"Total cost: {cost}")
