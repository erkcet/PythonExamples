"""Find connected components in an undirected graph."""


def connected_components(graph, all_nodes):
    """Return a list of sets, each set being a connected component."""
    visited = set()
    components = []

    def _dfs(node, comp):
        visited.add(node)
        comp.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor, comp)

    for node in all_nodes:
        if node not in visited:
            comp = set()
            _dfs(node, comp)
            components.append(comp)
    return components


if __name__ == "__main__":
    graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
    comps = connected_components(graph, range(5))
    for i, c in enumerate(comps):
        print(f"Component {i}: {sorted(c)}")
