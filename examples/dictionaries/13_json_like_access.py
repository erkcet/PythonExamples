"""Dot-notation access for dictionaries (attribute-style)."""


class DotDict(dict):
    """Dictionary that supports attribute-style access."""

    def __getattr__(self, key):
        try:
            val = self[key]
            return DotDict(val) if isinstance(val, dict) else val
        except KeyError:
            raise AttributeError(f"No attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError(f"No attribute '{key}'")


def from_nested_dict(d):
    """Convert a nested dict to DotDict recursively."""
    if isinstance(d, dict):
        return DotDict({k: from_nested_dict(v) for k, v in d.items()})
    return d


if __name__ == "__main__":
    config = DotDict({"host": "localhost", "port": 8080})
    print(f"config.host = {config.host}")
    config.debug = True
    print(f"config['debug'] = {config['debug']}")
    nested = from_nested_dict({"db": {"host": "localhost", "creds": {"user": "admin"}}})
    print(f"nested.db.creds.user = {nested.db.creds.user}")
    print(f"As dict: {dict(nested)}")
