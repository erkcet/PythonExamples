"""HMAC message signing and verification."""

import hmac
import hashlib


def sign_message(key, message, algorithm="sha256"):
    """Create an HMAC signature for a message."""
    return hmac.new(
        key.encode("utf-8"), message.encode("utf-8"), getattr(hashlib, algorithm)
    ).hexdigest()


def verify_signature(key, message, signature, algorithm="sha256"):
    """Verify an HMAC signature (timing-attack safe)."""
    expected = sign_message(key, message, algorithm)
    return hmac.compare_digest(expected, signature)


def sign_payload(key, payload_parts):
    """Sign a multi-part payload by joining parts."""
    message = "&".join(f"{k}={v}" for k, v in sorted(payload_parts.items()))
    return message, sign_message(key, message)


if __name__ == "__main__":
    secret = "my-secret-key"
    msg = "Important data to protect"
    sig = sign_message(secret, msg)
    print(f"Message:   {msg}")
    print(f"Signature: {sig}")
    print(f"Valid:     {verify_signature(secret, msg, sig)}")
    print(f"Tampered:  {verify_signature(secret, msg + '!', sig)}")
    payload = {"user": "alice", "action": "transfer", "amount": "100"}
    canonical, psig = sign_payload(secret, payload)
    print(f"\nPayload: {canonical}")
    print(f"Signed:  {psig}")
