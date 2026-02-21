"""Generate a URL-friendly slug from a string."""

import re


def generate_slug(text):
    """Convert text to a URL-friendly slug."""
    slug = text.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug)
    slug = slug.strip('-')
    return slug


if __name__ == "__main__":
    titles = [
        "Hello, World!",
        "  My Blog Post Title  ",
        "Python 3.12: What's New?",
        "100% Working -- Solution!!!",
    ]
    for title in titles:
        print(f"'{title}' -> '{generate_slug(title)}'")
