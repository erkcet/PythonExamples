"""Dijkstra's shortest-path algorithm."""

import heapq


def dijkstra(graph, start):
    """Return shortest distances from *start* to all reachable nodes.

    Args:
        graph: dict mapping node -> list of (neighbor, weight).
    """
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    distances = dijkstra(graph, "A")
    for node, d in sorted(distances.items()):
        print(f"A -> {node}: {d}")
