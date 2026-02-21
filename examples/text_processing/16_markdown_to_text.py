"""Convert simple Markdown to plain text by stripping formatting."""

import re


def markdown_to_text(md):
    """Strip common Markdown formatting and return plain text."""
    text = md
    # Remove headers (## Header -> Header)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic
    text = re.sub(r'\*{1,3}(.+?)\*{1,3}', r'\1', text)
    text = re.sub(r'_{1,3}(.+?)_{1,3}', r'\1', text)
    # Convert links [text](url) -> text
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    # Remove inline code backticks
    text = re.sub(r'`(.+?)`', r'\1', text)
    # Convert list items
    text = re.sub(r'^\s*[-*+]\s+', '  - ', text, flags=re.MULTILINE)
    return text


if __name__ == "__main__":
    markdown = """# Welcome to Python
This is **bold** and *italic* text.
Check out [Python docs](https://python.org) for more.
Use `print()` to output text.

## Features
- Simple syntax
- **Powerful** libraries
- Great community
"""
    print("Markdown -> Plain text:")
    print(markdown_to_text(markdown))
