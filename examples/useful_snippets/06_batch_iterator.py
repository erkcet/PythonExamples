"""Process items in batches (chunked iteration)."""

from itertools import islice


def batch(iterable, size):
    """Yield successive batches of the given size."""
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        yield chunk


def batch_with_padding(iterable, size, fill=None):
    """Yield batches, padding the last one if needed."""
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        while len(chunk) < size:
            chunk.append(fill)
        yield chunk


def process_in_batches(items, batch_size, processor):
    """Process items in batches, returning all results."""
    results = []
    for i, chunk in enumerate(batch(items, batch_size)):
        result = processor(chunk)
        results.append(result)
    return results


if __name__ == "__main__":
    items = list(range(1, 12))
    print(f"Items: {items}")
    print(f"Batches of 3: {list(batch(items, 3))}")
    print(f"Padded batches: {list(batch_with_padding(items, 4, fill=0))}")
    results = process_in_batches(items, 4, lambda b: sum(b))
    print(f"Batch sums: {results}")
