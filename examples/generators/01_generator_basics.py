"""Basic generator with yield: lazy sequence production."""


def countdown(n):
    """Yield numbers from n down to 1."""
    while n > 0:
        yield n
        n -= 1


def range_squared(start, stop):
    """Yield squares of numbers in [start, stop)."""
    for i in range(start, stop):
        yield i ** 2


def words(sentence):
    """Yield individual words from a sentence."""
    for word in sentence.split():
        yield word.strip(".,!?")


if __name__ == "__main__":
    print("Countdown:", list(countdown(5)))
    print("Squares:", list(range_squared(1, 6)))

    for w in words("Hello, world! Python is great."):
        print(f"  Word: {w}")
