"""Validate email addresses using regular expressions."""

import re

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


def is_valid_email(email):
    """Check if a string is a valid email address."""
    return bool(EMAIL_PATTERN.match(email))


def extract_email_parts(email):
    """Extract local part and domain from an email."""
    match = re.match(r"^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$", email)
    if match:
        return {"local": match.group(1), "domain": match.group(2)}
    return None


def find_emails_in_text(text):
    """Find all email addresses in a block of text."""
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)


if __name__ == "__main__":
    test_emails = ["user@example.com", "bad@", "a.b+c@domain.org", "@missing.com", "x@y.co"]
    for email in test_emails:
        print(f"  {email:25s} -> valid: {is_valid_email(email)}")

    print("\nParts:", extract_email_parts("alice.bob+tag@mail.example.com"))

    text = "Reach out to support@company.com or sales@company.org for help."
    print("Found emails:", find_emails_in_text(text))
