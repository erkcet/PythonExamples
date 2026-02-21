"""Topological sorting of a directed acyclic graph (DAG)."""

from collections import deque


def topological_sort(graph, all_nodes):
    """Return a topological ordering using Kahn's algorithm.

    Args:
        graph: dict mapping node -> list of neighbors (directed edges).
        all_nodes: iterable of every node in the graph.
    """
    in_degree = {n: 0 for n in all_nodes}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = deque(n for n in all_nodes if in_degree[n] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for v in graph.get(node, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(order) != len(all_nodes):
        raise ValueError("Graph contains a cycle")
    return order


if __name__ == "__main__":
    dag = {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: []}
    print(f"Topological order: {topological_sort(dag, range(5))}")
