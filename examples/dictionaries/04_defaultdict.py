"""Using collections.defaultdict for automatic default values."""

from collections import defaultdict


def group_words_by_length(words):
    """Group words by their length."""
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def build_adjacency_list(edges):
    """Build a graph adjacency list from edge pairs."""
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return {k: sorted(v) for k, v in graph.items()}


def count_items(items):
    """Count items using defaultdict(int)."""
    counts = defaultdict(int)
    for item in items:
        counts[item] += 1
    return dict(counts)


def nested_defaultdict():
    """Create a two-level defaultdict for tabular data."""
    table = defaultdict(lambda: defaultdict(int))
    table["Alice"]["math"] = 95
    table["Alice"]["science"] = 88
    table["Bob"]["math"] = 72
    return {k: dict(v) for k, v in table.items()}


if __name__ == "__main__":
    words = ["hi", "hello", "hey", "world", "python", "go"]
    print(f"By length: {group_words_by_length(words)}")
    edges = [("A", "B"), ("B", "C"), ("A", "C")]
    print(f"Graph: {build_adjacency_list(edges)}")
    print(f"Counts: {count_items('abracadabra')}")
    print(f"Nested: {nested_defaultdict()}")
