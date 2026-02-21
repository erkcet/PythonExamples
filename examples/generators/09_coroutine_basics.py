"""Basic coroutine patterns using generators."""


def coroutine(func):
    """Decorator to auto-prime a coroutine generator."""
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper


@coroutine
def printer(prefix):
    """Coroutine that prints received values with a prefix."""
    while True:
        value = yield
        print(f"{prefix}: {value}")


@coroutine
def filter_coroutine(predicate, target):
    """Coroutine that filters values before forwarding to target."""
    while True:
        value = yield
        if predicate(value):
            target.send(value)


@coroutine
def averager():
    """Coroutine that tracks and yields running average."""
    total = 0.0
    count = 0
    while True:
        value = yield total / count if count else 0
        total += value
        count += 1


if __name__ == "__main__":
    p = printer("Got")
    p.send("Hello")
    p.send(42)

    sink = printer("Even")
    pipe = filter_coroutine(lambda x: x % 2 == 0, sink)
    for i in range(10):
        pipe.send(i)
