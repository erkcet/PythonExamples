"""Sieve of Eratosthenes for finding primes."""


def sieve(limit: int) -> list[int]:
    """Return all prime numbers up to limit using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def prime_count(limit: int) -> int:
    """Return the count of primes up to limit."""
    return len(sieve(limit))


def nth_prime(n: int) -> int:
    """Return the nth prime number (1-indexed)."""
    upper = max(20, n * 15)
    primes = sieve(upper)
    while len(primes) < n:
        upper *= 2
        primes = sieve(upper)
    return primes[n - 1]


if __name__ == "__main__":
    print(f"Primes up to 50: {sieve(50)}")
    print(f"Number of primes under 1000: {prime_count(1000)}")
    for i in [1, 10, 100, 1000]:
        print(f"Prime #{i}: {nth_prime(i)}")
