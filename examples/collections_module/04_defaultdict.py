"""defaultdict patterns for automatic default values."""

from collections import defaultdict


def group_by_first_letter(words):
    """Group words by their first letter."""
    groups = defaultdict(list)
    for word in words:
        groups[word[0].lower()].append(word)
    return dict(groups)


def count_items(items):
    """Count items using defaultdict(int)."""
    counts = defaultdict(int)
    for item in items:
        counts[item] += 1
    return dict(counts)


def build_graph(edges):
    """Build an adjacency list from edge pairs."""
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return {k: sorted(v) for k, v in graph.items()}


if __name__ == "__main__":
    words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
    print("Grouped:", group_by_first_letter(words))

    items = ["cat", "dog", "cat", "bird", "dog", "cat"]
    print("\nCounts:", count_items(items))

    edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]
    print("\nGraph:", build_graph(edges))

    # Nested defaultdict
    nested = defaultdict(lambda: defaultdict(int))
    nested["fruits"]["apple"] = 5
    nested["fruits"]["banana"] = 3
    print(f"\nNested: {dict(nested['fruits'])}")
