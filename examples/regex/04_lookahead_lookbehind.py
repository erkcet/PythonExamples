"""Lookahead and lookbehind assertions in regular expressions."""

import re


def positive_lookahead(text):
    """Find words followed by a specific pattern."""
    return re.findall(r"\w+(?=\sprice)", text)


def negative_lookahead(text):
    """Find digits NOT followed by a percent sign."""
    return re.findall(r"\d+(?!%)", text)


def positive_lookbehind(text):
    """Find amounts preceded by a dollar sign."""
    return re.findall(r"(?<=\$)\d+(?:\.\d{2})?", text)


def negative_lookbehind(text):
    """Find digits NOT preceded by a hash."""
    return re.findall(r"(?<!#)\b\d+\b", text)


def password_strength(password):
    """Check password strength using multiple lookaheads."""
    checks = {
        "has_upper": bool(re.search(r"(?=.*[A-Z])", password)),
        "has_lower": bool(re.search(r"(?=.*[a-z])", password)),
        "has_digit": bool(re.search(r"(?=.*\d)", password)),
        "min_length": bool(re.search(r"(?=.{8,})", password)),
    }
    return checks


if __name__ == "__main__":
    print("Lookahead:", positive_lookahead("best price and sale price"))
    print("Neg lookahead:", negative_lookahead("50% off, save 30 dollars"))
    print("Lookbehind:", positive_lookbehind("Items: $19.99 and $5.00"))
    print("Neg lookbehind:", negative_lookbehind("Color #123 and 456"))
    print("Password check:", password_strength("Secret42"))
