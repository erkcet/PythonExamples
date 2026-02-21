"""Search for words in text and highlight them with markers."""


def highlight(text, keyword, marker_start=">>", marker_end="<<"):
    """Highlight all occurrences of keyword in text (case-insensitive)."""
    result = []
    lower_text = text.lower()
    lower_key = keyword.lower()
    i = 0
    while i < len(text):
        if lower_text[i:i+len(lower_key)] == lower_key:
            result.append(marker_start)
            result.append(text[i:i+len(keyword)])
            result.append(marker_end)
            i += len(keyword)
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)


if __name__ == "__main__":
    text = "Python is great. I love Python programming. python is easy."
    keyword = "python"
    print(f"Original: {text}")
    print(f"Search:   '{keyword}'")
    print(f"Result:   {highlight(text, keyword)}")
    print(f"Caps:     {highlight(text, keyword, '[', ']')}")
