"""Convert strings to title case with proper handling of small words."""


SMALL_WORDS = {"a", "an", "the", "and", "but", "or", "for", "nor",
               "on", "at", "to", "in", "of", "with", "by"}


def title_case(s):
    """Convert to title case, keeping small words lowercase unless first."""
    words = s.lower().split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word not in SMALL_WORDS:
            result.append(word.capitalize())
        else:
            result.append(word)
    return ' '.join(result)


if __name__ == "__main__":
    titles = [
        "the lord of the rings",
        "a tale of two cities",
        "war and peace",
    ]
    for t in titles:
        print(f"'{t}' -> '{title_case(t)}'")
