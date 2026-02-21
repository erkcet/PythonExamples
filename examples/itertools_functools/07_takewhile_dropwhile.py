"""itertools.takewhile and dropwhile for conditional slicing."""

import itertools


def take_while_positive(numbers):
    """Take elements from the start while they are positive."""
    return list(itertools.takewhile(lambda x: x > 0, numbers))


def drop_while_small(numbers, threshold):
    """Drop elements from the start while they are below threshold."""
    return list(itertools.dropwhile(lambda x: x < threshold, numbers))


def parse_header_body(lines):
    """Split lines into header (non-empty) and body (after first blank)."""
    it = iter(lines)
    header = list(itertools.takewhile(lambda l: l.strip(), it))
    body = list(it)  # remaining lines after the blank
    return header, body


def take_until(predicate, iterable):
    """Take elements until predicate becomes True (inclusive)."""
    for item in iterable:
        yield item
        if predicate(item):
            break


if __name__ == "__main__":
    nums = [3, 7, 2, -1, 5, 8]
    print("Take while positive:", take_while_positive(nums))

    data = [1, 3, 5, 10, 2, 15]
    print("Drop while < 5:", drop_while_small(data, 5))

    message = ["From: Alice", "To: Bob", "", "Hello!", "How are you?"]
    header, body = parse_header_body(message)
    print(f"\nHeader: {header}")
    print(f"Body: {body}")

    print("Take until > 5:", list(take_until(lambda x: x > 5, [1, 3, 7, 2, 9])))
