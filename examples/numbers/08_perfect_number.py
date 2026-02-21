"""Check perfect number."""


def divisor_sum(n: int) -> int:
    """Return the sum of proper divisors of n."""
    if n < 2:
        return 0
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total


def is_perfect(n: int) -> bool:
    """Return True if n equals the sum of its proper divisors."""
    return n > 1 and divisor_sum(n) == n


def classify_number(n: int) -> str:
    """Classify as perfect, abundant, or deficient."""
    s = divisor_sum(n)
    if s == n:
        return "perfect"
    return "abundant" if s > n else "deficient"


if __name__ == "__main__":
    for num in [6, 12, 28, 33, 496, 8128]:
        print(f"{num:>5}: divisor sum={divisor_sum(num):<5} -> {classify_number(num)}")
    print("\nPerfect numbers under 10000:",
          [n for n in range(2, 10000) if is_perfect(n)])
