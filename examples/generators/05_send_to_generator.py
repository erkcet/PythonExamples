"""Using send() to communicate with a running generator."""


def accumulator():
    """Generator that accumulates values sent to it."""
    total = 0
    while True:
        value = yield total
        if value is None:
            return
        total += value


def running_average():
    """Generator that computes a running average via send()."""
    total = 0.0
    count = 0
    avg = 0.0
    while True:
        value = yield avg
        if value is None:
            return
        total += value
        count += 1
        avg = total / count


if __name__ == "__main__":
    acc = accumulator()
    next(acc)  # prime the generator
    print(f"Send 10: {acc.send(10)}")
    print(f"Send 20: {acc.send(20)}")
    print(f"Send 5:  {acc.send(5)}")

    avg = running_average()
    next(avg)  # prime
    for val in [10, 20, 30, 40]:
        result = avg.send(val)
        print(f"Sent {val}, running avg = {result:.1f}")
