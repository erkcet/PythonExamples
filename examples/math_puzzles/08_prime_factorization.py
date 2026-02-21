"""Prime factorization of integers."""


def prime_factors(n):
    """Return the prime factorization as a list of (prime, exponent) tuples."""
    factors = []
    d = 2
    while d * d <= n:
        exp = 0
        while n % d == 0:
            n //= d
            exp += 1
        if exp > 0:
            factors.append((d, exp))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def factorization_string(n):
    """Return a readable factorization string like '2^3 x 3 x 5^2'."""
    factors = prime_factors(n)
    parts = [f"{p}^{e}" if e > 1 else str(p) for p, e in factors]
    return " x ".join(parts)


def num_divisors(n):
    """Count the number of divisors using prime factorization."""
    count = 1
    for _, exp in prime_factors(n):
        count *= (exp + 1)
    return count


def sum_divisors(n):
    """Sum all divisors using prime factorization."""
    total = 1
    for p, e in prime_factors(n):
        total *= (p ** (e + 1) - 1) // (p - 1)
    return total


if __name__ == "__main__":
    for n in [12, 60, 97, 360, 1000, 2**10]:
        print(f"{n:5d} = {factorization_string(n):20s}  divisors={num_divisors(n)}")
    print(f"\nDivisor sum of 12: {sum_divisors(12)} (1+2+3+4+6+12={1+2+3+4+6+12})")
