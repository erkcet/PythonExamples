"""Closures and the nonlocal keyword."""


def make_counter(start=0):
    """Create a counter closure that increments on each call."""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


def make_accumulator():
    """Create a closure that accumulates a running total."""
    total = 0

    def add(value):
        nonlocal total
        total += value
        return total

    return add


def make_greeting(prefix):
    """Closure capturing prefix from the enclosing scope."""
    def greeter(name):
        return f"{prefix}, {name}!"
    return greeter


if __name__ == "__main__":
    counter = make_counter(10)
    print(counter(), counter(), counter())

    acc = make_accumulator()
    for v in [5, 10, 15]:
        print(f"Added {v}, total = {acc(v)}")

    hi = make_greeting("Hi")
    print(hi("Alice"))
