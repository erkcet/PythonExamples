"""Calculate Pearson correlation coefficient."""

import math


def mean(data: list[float]) -> float:
    """Calculate arithmetic mean."""
    return sum(data) / len(data)


def correlation(x: list[float], y: list[float]) -> float:
    """Calculate Pearson correlation coefficient between x and y."""
    if len(x) != len(y):
        raise ValueError("Lists must have equal length")
    n = len(x)
    mx, my = mean(x), mean(y)
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den_x = math.sqrt(sum((xi - mx) ** 2 for xi in x))
    den_y = math.sqrt(sum((yi - my) ** 2 for yi in y))
    if den_x == 0 or den_y == 0:
        return 0.0
    return num / (den_x * den_y)


def interpret(r: float) -> str:
    """Interpret the correlation coefficient."""
    ar = abs(r)
    if ar >= 0.8: strength = "very strong"
    elif ar >= 0.6: strength = "strong"
    elif ar >= 0.4: strength = "moderate"
    elif ar >= 0.2: strength = "weak"
    else: strength = "very weak"
    direction = "positive" if r > 0 else "negative"
    return f"{strength} {direction}"


if __name__ == "__main__":
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [2, 4, 5, 4, 5, 7, 8, 9, 10, 12]
    r = correlation(x1, y1)
    print(f"X: {x1}")
    print(f"Y: {y1}")
    print(f"r = {r:.4f} ({interpret(r)})")

    y2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    r2 = correlation(x1, y2)
    print(f"\nPerfect negative: r = {r2:.4f} ({interpret(r2)})")
