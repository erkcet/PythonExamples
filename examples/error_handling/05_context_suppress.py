"""Using contextlib.suppress to ignore specific exceptions."""

import contextlib
import os


def remove_file_safe(path):
    """Remove a file, ignoring FileNotFoundError."""
    with contextlib.suppress(FileNotFoundError):
        os.remove(path)
        print(f"Removed: {path}")
    print(f"remove_file_safe('{path}') complete")


def get_from_dict(data, *keys):
    """Get nested dict value, returning None on missing keys."""
    result = data
    for key in keys:
        with contextlib.suppress(KeyError, TypeError):
            result = result[key]
            continue
        return None
    return result


def safe_parse_int(value):
    """Parse int, returning None on failure."""
    with contextlib.suppress(ValueError, TypeError):
        return int(value)
    return None


if __name__ == "__main__":
    remove_file_safe("/tmp/nonexistent_file.txt")
    data = {"a": {"b": {"c": 42}}}
    print(f"Nested lookup: {get_from_dict(data, 'a', 'b', 'c')}")
    print(f"Missing path: {get_from_dict(data, 'a', 'x')}")
    print(f"Parse '99': {safe_parse_int('99')}")
    print(f"Parse 'no': {safe_parse_int('no')}")
