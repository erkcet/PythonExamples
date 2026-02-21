"""Check if a number is prime."""

import math


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def primes_up_to(n: int) -> list[int]:
    """Return all primes up to n."""
    return [i for i in range(2, n + 1) if is_prime(i)]


if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 17, 25, 97, 100]
    for num in test_numbers:
        status = "prime" if is_prime(num) else "not prime"
        print(f"{num:>4} is {status}")
    print(f"\nPrimes up to 50: {primes_up_to(50)}")
