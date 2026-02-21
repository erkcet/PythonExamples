"""Capitalize the first letter of every word in a string."""


def capitalize_words(s):
    """Capitalize each word manually without str.title()."""
    words = s.split()
    result = []
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
    return ' '.join(result)


if __name__ == "__main__":
    sentences = [
        "hello world",
        "python is awesome",
        "the quick brown fox",
    ]
    for sentence in sentences:
        print(f"'{sentence}' -> '{capitalize_words(sentence)}'")
