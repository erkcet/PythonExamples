"""UUID generation using the uuid module."""

import uuid


def generate_uuid4():
    """Generate a random UUID (version 4)."""
    return str(uuid.uuid4())


def generate_uuid1():
    """Generate a time-based UUID (version 1)."""
    return str(uuid.uuid1())


def generate_uuid5(namespace, name):
    """Generate a deterministic UUID (version 5, SHA-1)."""
    ns_map = {"dns": uuid.NAMESPACE_DNS, "url": uuid.NAMESPACE_URL}
    ns = ns_map.get(namespace, uuid.NAMESPACE_DNS)
    return str(uuid.uuid5(ns, name))


def parse_uuid(uuid_str):
    """Parse and analyze a UUID string."""
    u = uuid.UUID(uuid_str)
    return {
        "hex": u.hex, "version": u.version,
        "variant": str(u.variant), "int": u.int,
        "bytes": u.bytes.hex(),
    }


if __name__ == "__main__":
    u4 = generate_uuid4()
    print(f"UUID v4 (random):    {u4}")
    print(f"UUID v1 (time):      {generate_uuid1()}")
    print(f"UUID v5 (DNS/test):  {generate_uuid5('dns', 'example.com')}")
    print(f"UUID v5 (same):      {generate_uuid5('dns', 'example.com')}")
    print(f"\nParsed: {parse_uuid(u4)}")
