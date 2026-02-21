"""Using re.compile for performance with repeated pattern usage."""

import re
import timeit

# Compile patterns once for reuse
WORD_PATTERN = re.compile(r"\b\w+\b")
INT_PATTERN = re.compile(r"-?\d+")
CSV_PATTERN = re.compile(r",\s*")


def count_words(text):
    """Count words using a compiled pattern."""
    return len(WORD_PATTERN.findall(text))


def extract_integers(text):
    """Extract all integers using a compiled pattern."""
    return [int(x) for x in INT_PATTERN.findall(text)]


def smart_split(csv_line):
    """Split CSV handling optional whitespace after commas."""
    return CSV_PATTERN.split(csv_line)


def benchmark_compiled_vs_inline():
    """Compare compiled vs inline regex performance."""
    text = "Hello world 123 test " * 100
    compiled = re.compile(r"\d+")

    t_compiled = timeit.timeit(lambda: compiled.findall(text), number=1000)
    t_inline = timeit.timeit(lambda: re.findall(r"\d+", text), number=1000)
    return {"compiled": round(t_compiled, 4), "inline": round(t_inline, 4)}


if __name__ == "__main__":
    sample = "There are 12 apples, -3 oranges, and 100 bananas."
    print("Word count:", count_words(sample))
    print("Integers:", extract_integers(sample))
    print("Smart split:", smart_split("a, b,c,  d, e"))
    print("Benchmark:", benchmark_compiled_vs_inline())
