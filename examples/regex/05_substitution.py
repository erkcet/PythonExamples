"""Regex substitution with re.sub and re.subn."""

import re


def censor_emails(text):
    """Replace email addresses with [REDACTED]."""
    return re.sub(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", "[REDACTED]", text)


def normalize_whitespace(text):
    """Replace multiple whitespace with a single space."""
    return re.sub(r"\s+", " ", text.strip())


def camel_to_snake(name):
    """Convert camelCase to snake_case using re.sub."""
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s1).lower()


def substitute_with_function(text):
    """Use a function as replacement in re.sub."""
    def double_number(match):
        return str(int(match.group()) * 2)
    return re.sub(r"\d+", double_number, text)


if __name__ == "__main__":
    print("Censor:", censor_emails("Contact us at info@test.com or help@test.org"))
    print("Normalize:", normalize_whitespace("  too   many   spaces  "))
    print("Snake case:", camel_to_snake("myVariableName"))
    print("Double nums:", substitute_with_function("I have 3 cats and 5 dogs"))

    # re.subn returns count of replacements
    result, count = re.subn(r"\d", "#", "abc123def456")
    print(f"subn result: {result}, replacements: {count}")
