"""Breadth-first search traversal of a graph."""

from collections import deque


def bfs(graph, start):
    """Return nodes in BFS order starting from *start*.

    Args:
        graph: dict mapping node -> list of neighbors.
        start: starting node.
    """
    visited, order, queue = set(), [], deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
    print(f"BFS from 0: {bfs(graph, 0)}")
