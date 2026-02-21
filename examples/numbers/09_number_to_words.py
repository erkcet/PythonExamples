"""Convert number to words."""

ONES = ["", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
SCALES = ["", "thousand", "million", "billion", "trillion"]


def number_to_words(n: int) -> str:
    """Convert an integer to its English word representation."""
    if n == 0:
        return "zero"
    if n < 0:
        return "negative " + number_to_words(-n)

    def chunk_to_words(num: int) -> str:
        if num == 0:
            return ""
        if num < 20:
            return ONES[num]
        if num < 100:
            return TENS[num // 10] + ("-" + ONES[num % 10] if num % 10 else "")
        return ONES[num // 100] + " hundred" + (" " + chunk_to_words(num % 100) if num % 100 else "")

    parts, scale_idx = [], 0
    while n > 0:
        chunk = n % 1000
        if chunk:
            word = chunk_to_words(chunk)
            if SCALES[scale_idx]:
                word += " " + SCALES[scale_idx]
            parts.append(word)
        n //= 1000
        scale_idx += 1
    return " ".join(reversed(parts))


if __name__ == "__main__":
    tests = [0, 5, 13, 42, 100, 305, 1024, 1000000, -99]
    for num in tests:
        print(f"{num:>10} -> {number_to_words(num)}")
