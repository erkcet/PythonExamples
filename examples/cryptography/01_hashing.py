"""MD5 and SHA256 hashing with hashlib."""

import hashlib


def hash_string(text, algorithm="sha256"):
    """Hash a string using the specified algorithm."""
    h = hashlib.new(algorithm)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def hash_file(filepath, algorithm="sha256", chunk_size=8192):
    """Compute hash of a file without loading it entirely into memory."""
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def compare_hashes(text, expected_hash, algorithm="sha256"):
    """Verify a string matches an expected hash."""
    return hash_string(text, algorithm) == expected_hash


if __name__ == "__main__":
    msg = "Hello, World!"
    md5 = hash_string(msg, "md5")
    sha256 = hash_string(msg, "sha256")
    sha512 = hash_string(msg, "sha512")
    print(f"Message:  {msg}")
    print(f"MD5:      {md5}")
    print(f"SHA-256:  {sha256}")
    print(f"SHA-512:  {sha512}")
    print(f"Verify:   {compare_hashes(msg, sha256)}")
    print(f"Available: {sorted(hashlib.algorithms_guaranteed)}")
