"""Calculate mean, median, and mode."""

from collections import Counter


def mean(data: list[float]) -> float:
    """Calculate the arithmetic mean."""
    if not data:
        raise ValueError("Empty dataset")
    return sum(data) / len(data)


def median(data: list[float]) -> float:
    """Calculate the median value."""
    if not data:
        raise ValueError("Empty dataset")
    s = sorted(data)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2


def mode(data: list[float]) -> list[float]:
    """Return the mode(s) -- most frequently occurring value(s)."""
    if not data:
        raise ValueError("Empty dataset")
    counts = Counter(data)
    max_count = max(counts.values())
    return sorted(k for k, v in counts.items() if v == max_count)


if __name__ == "__main__":
    dataset = [4, 7, 2, 7, 9, 1, 7, 3, 2, 8]
    print(f"Data:   {dataset}")
    print(f"Mean:   {mean(dataset):.2f}")
    print(f"Median: {median(dataset):.2f}")
    print(f"Mode:   {mode(dataset)}")
