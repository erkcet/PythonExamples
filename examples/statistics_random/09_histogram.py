"""Text-based histogram."""

from collections import Counter


def histogram(data: list[float], bins: int = 10) -> None:
    """Print a text-based histogram of numeric data."""
    min_val, max_val = min(data), max(data)
    bin_width = (max_val - min_val) / bins
    counts = [0] * bins
    for val in data:
        idx = min(int((val - min_val) / bin_width), bins - 1)
        counts[idx] += 1

    max_count = max(counts)
    for i in range(bins):
        lo = min_val + i * bin_width
        hi = lo + bin_width
        bar = "#" * int(counts[i] / max_count * 40) if max_count else ""
        print(f"  [{lo:6.1f}, {hi:6.1f}) | {counts[i]:>4} {bar}")


def frequency_chart(items: list[str], width: int = 40) -> None:
    """Print a horizontal bar chart from categorical data."""
    counts = Counter(items)
    max_count = max(counts.values())
    for item, count in counts.most_common():
        bar = "#" * int(count / max_count * width)
        print(f"  {item:>10}: {count:>3} {bar}")


if __name__ == "__main__":
    import random
    random.seed(42)
    data = [random.gauss(50, 15) for _ in range(500)]
    print("Normal distribution (mu=50, sigma=15):")
    histogram(data, bins=8)

    print("\nFruit frequency:")
    fruits = random.choices(["apple", "banana", "cherry", "date"], weights=[4, 3, 2, 1], k=100)
    frequency_chart(fruits)
