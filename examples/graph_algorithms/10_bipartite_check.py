"""Check whether an undirected graph is bipartite (2-colorable)."""

from collections import deque


def is_bipartite(graph, all_nodes):
    """Return True if the graph is bipartite.

    Uses BFS coloring: try to 2-color every connected component.
    """
    color = {}
    for start in all_nodes:
        if start in color:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True


if __name__ == "__main__":
    bipartite = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
    not_bipartite = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print(f"Even cycle bipartite: {is_bipartite(bipartite, range(4))}")
    print(f"Triangle bipartite:   {is_bipartite(not_bipartite, range(3))}")
