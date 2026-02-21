"""Recursive Power Function (Fast Exponentiation).

Computes base^exp using the divide-and-conquer approach.
O(log n) time instead of O(n) for naive multiplication.
"""


def power(base: float, exp: int) -> float:
    """Compute base^exp using fast exponentiation."""
    if exp == 0:
        return 1
    if exp < 0:
        return 1.0 / power(base, -exp)
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        return base * power(base, exp - 1)


def mod_power(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) % mod using fast modular exponentiation."""
    if exp == 0:
        return 1 % mod
    if exp % 2 == 0:
        half = mod_power(base, exp // 2, mod)
        return (half * half) % mod
    else:
        return (base * mod_power(base, exp - 1, mod)) % mod


if __name__ == "__main__":
    print(f"2^10 = {power(2, 10)}")
    print(f"3^(-3) = {power(3, -3):.6f}")
    print(f"5^0 = {power(5, 0)}")
    print(f"2^100 mod 1000000007 = {mod_power(2, 100, 1000000007)}")
