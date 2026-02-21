"""Split a list into fixed-size chunks."""

from itertools import islice


def chunk_slice(lst, size):
    """Chunk using simple slicing."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def chunk_iter(iterable, size):
    """Chunk any iterable using itertools.islice."""
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        yield chunk


def chunk_with_padding(lst, size, fill=None):
    """Chunk with padding for the last incomplete chunk."""
    chunks = chunk_slice(lst, size)
    if chunks and len(chunks[-1]) < size:
        chunks[-1].extend([fill] * (size - len(chunks[-1])))
    return chunks


if __name__ == "__main__":
    data = list(range(1, 11))
    print(f"Original: {data}")
    print(f"Chunks of 3: {chunk_slice(data, 3)}")
    print(f"Iter chunks: {list(chunk_iter(data, 4))}")
    print(f"Padded (3):  {chunk_with_padding(data, 3)}")
