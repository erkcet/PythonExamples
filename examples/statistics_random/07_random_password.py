"""Generate random passwords."""

import random
import string


def generate_password(length: int = 16, use_special: bool = True) -> str:
    """Generate a random password of the given length."""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


def generate_passphrase(num_words: int = 4, separator: str = "-") -> str:
    """Generate a passphrase from random common words."""
    words = [
        "apple", "brave", "cloud", "dance", "eagle", "flame", "grape",
        "house", "ivory", "judge", "knife", "lemon", "maple", "north",
        "ocean", "piano", "queen", "river", "stone", "tiger", "umbra",
        "vivid", "whale", "yield", "zebra", "amber", "bloom", "cedar",
    ]
    return separator.join(random.choice(words) for _ in range(num_words))


def password_strength(password: str) -> str:
    """Rate password strength as weak, medium, or strong."""
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    return ["weak", "weak", "medium", "medium", "strong", "strong"][score]


if __name__ == "__main__":
    random.seed(42)
    for length in [8, 12, 16]:
        pw = generate_password(length)
        print(f"Password ({length:>2}): {pw}  [{password_strength(pw)}]")
    print(f"\nPassphrase:   {generate_passphrase()}")
    print(f"Passphrase:   {generate_passphrase(5, '.')}")
