"""Generate cryptographically secure random tokens."""

import secrets
import string


def generate_token_hex(nbytes=32):
    """Generate a random hex token."""
    return secrets.token_hex(nbytes)


def generate_token_urlsafe(nbytes=32):
    """Generate a URL-safe random token."""
    return secrets.token_urlsafe(nbytes)


def generate_password(length=16, include_symbols=True):
    """Generate a secure random password."""
    alphabet = string.ascii_letters + string.digits
    if include_symbols:
        alphabet += string.punctuation
    while True:
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password)):
            return password


def generate_otp(length=6):
    """Generate a numeric one-time password."""
    return "".join(secrets.choice(string.digits) for _ in range(length))


if __name__ == "__main__":
    print(f"Hex token:     {generate_token_hex(16)}")
    print(f"URL-safe:      {generate_token_urlsafe(16)}")
    print(f"Password:      {generate_password(20)}")
    print(f"Simple pass:   {generate_password(12, include_symbols=False)}")
    print(f"OTP:           {generate_otp()}")
    print(f"Random bits:   {secrets.randbits(128)}")
