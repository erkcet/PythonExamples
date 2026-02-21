"""Classic FizzBuzz problem."""


def fizzbuzz(n):
    """Return FizzBuzz result for a single number."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_range(start, end):
    """Generate FizzBuzz for a range of numbers."""
    return [fizzbuzz(i) for i in range(start, end + 1)]


def custom_fizzbuzz(n, rules):
    """FizzBuzz with custom divisor-word rules."""
    result = ""
    for divisor, word in sorted(rules.items()):
        if n % divisor == 0:
            result += word
    return result or str(n)


if __name__ == "__main__":
    print("FizzBuzz 1-20:")
    print(", ".join(fizzbuzz_range(1, 20)))
    print("\nCustom rules {3:Fizz, 5:Buzz, 7:Jazz}:")
    rules = {3: "Fizz", 5: "Buzz", 7: "Jazz"}
    results = [custom_fizzbuzz(i, rules) for i in range(1, 22)]
    print(", ".join(results))
