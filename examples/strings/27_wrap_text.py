"""Wrap text to a specified line width, breaking at word boundaries."""

import textwrap


def wrap_text(text, width=40):
    """Wrap text at word boundaries to fit within width."""
    words = text.split()
    lines = []
    current_line = []
    current_len = 0
    for word in words:
        if current_len + len(word) + len(current_line) > width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_len = len(word)
        else:
            current_line.append(word)
            current_len += len(word)
    if current_line:
        lines.append(' '.join(current_line))
    return '\n'.join(lines)


if __name__ == "__main__":
    paragraph = ("Python is an interpreted high-level general-purpose programming "
                 "language. Its design philosophy emphasizes code readability with "
                 "the use of significant indentation.")
    print("Manual wrap (width=40):")
    print(wrap_text(paragraph, 40))
    print("\ntextwrap.fill (width=40):")
    print(textwrap.fill(paragraph, 40))
