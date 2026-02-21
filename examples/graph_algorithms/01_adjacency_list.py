"""Graph representation using an adjacency list."""


class Graph:
    """Undirected graph using a dict-based adjacency list."""

    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        """Add an undirected edge between u and v."""
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def neighbors(self, node):
        """Return neighbors of a node."""
        return self.adj.get(node, [])

    def __repr__(self):
        return "\n".join(f"{k}: {v}" for k, v in sorted(self.adj.items()))


if __name__ == "__main__":
    g = Graph()
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]:
        g.add_edge(u, v)
    print("Adjacency list:")
    print(g)
    print(f"Neighbors of 3: {g.neighbors(3)}")
