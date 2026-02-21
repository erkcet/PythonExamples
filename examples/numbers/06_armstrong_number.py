"""Check Armstrong number (narcissistic number)."""


def is_armstrong(n: int) -> bool:
    """Return True if n is an Armstrong number.

    An Armstrong number equals the sum of its digits each raised
    to the power of the number of digits.
    """
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


def find_armstrong_numbers(start: int, end: int) -> list[int]:
    """Find all Armstrong numbers in the given range."""
    return [n for n in range(start, end + 1) if is_armstrong(n)]


if __name__ == "__main__":
    test = [0, 1, 153, 370, 371, 407, 123, 9474]
    for num in test:
        result = "is" if is_armstrong(num) else "is not"
        print(f"{num:>5} {result} an Armstrong number")
    print(f"\nArmstrong numbers 1-999: {find_armstrong_numbers(1, 999)}")
