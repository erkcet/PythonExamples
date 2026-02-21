"""Chaining generators as a data processing pipeline."""


def integers(start=1):
    """Yield integers starting from start."""
    n = start
    while True:
        yield n
        n += 1


def evens(source):
    """Filter: yield only even numbers from source."""
    for n in source:
        yield n if n % 2 == 0 else None


def squared(source):
    """Transform: yield squared values, skip None."""
    for n in source:
        if n is not None:
            yield n ** 2


def take_while_under(limit, source):
    """Yield values from source while they are under limit."""
    for n in source:
        if n >= limit:
            return
        yield n


if __name__ == "__main__":
    # Pipeline: integers -> evens -> squared -> take while < 500
    pipeline = take_while_under(500, squared(evens(integers(1))))
    results = list(pipeline)
    print(f"Even squares under 500: {results}")
    print(f"Count: {len(results)}")
