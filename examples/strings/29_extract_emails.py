"""Extract email addresses from a block of text using regex."""

import re

EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')


def extract_emails(text):
    """Return a list of email addresses found in the text."""
    return EMAIL_PATTERN.findall(text)


if __name__ == "__main__":
    text = """
    Contact us at support@example.com or sales@company.org.
    You can also reach john.doe+work@mail.co.uk for inquiries.
    Invalid: user@, @domain.com, plain text.
    """
    emails = extract_emails(text)
    print("Found emails:")
    for email in emails:
        print(f"  {email}")
    print(f"Total: {len(emails)}")
