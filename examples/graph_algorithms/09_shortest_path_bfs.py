"""Shortest path in an unweighted graph using BFS."""

from collections import deque


def shortest_path(graph, start, end):
    """Return the shortest path from *start* to *end*, or None."""
    if start == end:
        return [start]
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1, 5], 4: [2, 5], 5: [3, 4]}
    path = shortest_path(graph, 0, 5)
    print(f"Shortest path 0 -> 5: {path}  (length {len(path) - 1})")
