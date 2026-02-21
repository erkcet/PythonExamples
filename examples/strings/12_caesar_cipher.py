"""Implement the Caesar cipher for encrypting and decrypting text."""


def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher with given shift."""
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def caesar_decrypt(text, shift):
    """Decrypt Caesar cipher by shifting in the opposite direction."""
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    message = "Hello, World!"
    shift = 3
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
