"""XOR cipher for educational purposes (NOT secure for production)."""


def xor_encrypt(plaintext, key):
    """Encrypt plaintext using XOR with a repeating key."""
    key_bytes = key.encode("utf-8")
    plain_bytes = plaintext.encode("utf-8")
    encrypted = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(plain_bytes))
    return encrypted.hex()


def xor_decrypt(hex_ciphertext, key):
    """Decrypt XOR-encrypted hex string (XOR is symmetric)."""
    cipher_bytes = bytes.fromhex(hex_ciphertext)
    key_bytes = key.encode("utf-8")
    decrypted = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(cipher_bytes))
    return decrypted.decode("utf-8")


def xor_bytes(data, key):
    """XOR raw bytes with a key (returns bytes)."""
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


if __name__ == "__main__":
    message = "Hello, XOR Cipher!"
    key = "secret"
    encrypted = xor_encrypt(message, key)
    decrypted = xor_decrypt(encrypted, key)
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Match:     {message == decrypted}")
    print("\nNote: XOR cipher is NOT secure - for educational use only!")
