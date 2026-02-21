"""Depth-first search traversal of a graph."""


def dfs_iterative(graph, start):
    """Return nodes in DFS order using an explicit stack."""
    visited, order, stack = set(), [], [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return order


def dfs_recursive(graph, node, visited=None):
    """Return nodes in DFS order using recursion."""
    if visited is None:
        visited = set()
    visited.add(node)
    result = [node]
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    return result


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
    print(f"DFS iterative from 0: {dfs_iterative(graph, 0)}")
    print(f"DFS recursive from 0: {dfs_recursive(graph, 0)}")
