"""Format raw text into properly spaced paragraphs."""

import textwrap


def format_paragraphs(text, width=60, indent="  "):
    """Format text into indented, wrapped paragraphs."""
    paragraphs = text.strip().split("\n\n")
    formatted = []
    for para in paragraphs:
        clean = ' '.join(para.split())
        wrapped = textwrap.fill(clean, width=width, initial_indent=indent,
                                subsequent_indent=indent)
        formatted.append(wrapped)
    return "\n\n".join(formatted)


if __name__ == "__main__":
    raw = """Python is a versatile programming language    that is widely used
for web development, data science,  automation, and more.

It features   dynamic typing, garbage collection,
and supports multiple programming   paradigms including
procedural, object-oriented,  and functional programming."""
    print("Formatted paragraphs:")
    print(format_paragraphs(raw, width=50))
