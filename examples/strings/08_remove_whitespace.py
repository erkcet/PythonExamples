"""Demonstrate different ways to remove whitespace from strings."""


def remove_all_whitespace(s):
    """Remove every whitespace character."""
    return ''.join(ch for ch in s if not ch.isspace())


def normalize_whitespace(s):
    """Replace multiple whitespace with a single space and strip ends."""
    return ' '.join(s.split())


if __name__ == "__main__":
    text = "  Hello   World  \t from \n Python  "
    print(f"Original:    repr={repr(text)}")
    print(f"Remove all:  '{remove_all_whitespace(text)}'")
    print(f"Normalized:  '{normalize_whitespace(text)}'")
    print(f"Stripped:    '{text.strip()}'")
