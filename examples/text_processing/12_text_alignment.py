"""Align text to the left, right, center, or justify it to a given width."""


def justify(text, width):
    """Full-justify text by distributing extra spaces between words."""
    words = text.split()
    if len(words) <= 1:
        return text.ljust(width)
    total_spaces = width - sum(len(w) for w in words)
    gaps = len(words) - 1
    base, extra = divmod(total_spaces, gaps)
    result = words[0]
    for i in range(1, len(words)):
        result += ' ' * (base + (1 if i <= extra else 0)) + words[i]
    return result


if __name__ == "__main__":
    text = "Hello World"
    w = 30
    b = "|"
    print(f"{b}{text.ljust(w)}{b}  <- left")
    print(f"{b}{text.rjust(w)}{b}  <- right")
    print(f"{b}{text.center(w)}{b}  <- center")
    phrase = "The quick brown fox jumps"
    print(f"{b}{justify(phrase, w)}{b}  <- justify")
