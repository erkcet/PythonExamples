"""Cycle detection in a directed graph using DFS coloring."""


def has_cycle(graph, all_nodes):
    """Return True if the directed graph contains a cycle.

    Uses white-gray-black coloring:
      0 = unvisited, 1 = in current path, 2 = fully processed.
    """
    color = {n: 0 for n in all_nodes}

    def _dfs(u):
        color[u] = 1
        for v in graph.get(u, []):
            if color[v] == 1:
                return True
            if color[v] == 0 and _dfs(v):
                return True
        color[u] = 2
        return False

    return any(color[n] == 0 and _dfs(n) for n in all_nodes)


if __name__ == "__main__":
    acyclic = {0: [1], 1: [2], 2: [3], 3: []}
    cyclic = {0: [1], 1: [2], 2: [0]}
    print(f"Acyclic graph has cycle: {has_cycle(acyclic, range(4))}")
    print(f"Cyclic  graph has cycle: {has_cycle(cyclic, range(3))}")
