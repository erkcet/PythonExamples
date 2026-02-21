"""Secure password hashing concepts using hashlib."""

import hashlib
import os
import hmac


def hash_password(password, salt=None, iterations=100_000):
    """Hash a password using PBKDF2-HMAC-SHA256."""
    if salt is None:
        salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return salt.hex() + ":" + dk.hex()


def verify_password(password, stored_hash, iterations=100_000):
    """Verify a password against a stored hash."""
    salt_hex, hash_hex = stored_hash.split(":")
    salt = bytes.fromhex(salt_hex)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(dk.hex(), hash_hex)


def password_strength(password):
    """Basic password strength checker."""
    checks = {
        "length >= 8": len(password) >= 8,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(not c.isalnum() for c in password),
    }
    return sum(checks.values()), checks


if __name__ == "__main__":
    pw = "MyS3cur3P@ss!"
    hashed = hash_password(pw)
    print(f"Hashed: {hashed[:60]}...")
    print(f"Verify correct: {verify_password(pw, hashed)}")
    print(f"Verify wrong:   {verify_password('wrong', hashed)}")
    score, details = password_strength(pw)
    print(f"Strength: {score}/5 - {details}")
