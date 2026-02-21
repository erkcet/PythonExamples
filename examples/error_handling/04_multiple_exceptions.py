"""Catching multiple exception types."""


def read_setting(config, key, as_type=int):
    """Read a config setting, handling multiple error types."""
    try:
        value = config[key]
        return as_type(value)
    except KeyError:
        print(f"Missing key: {key}")
    except (ValueError, TypeError) as e:
        print(f"Conversion error for '{key}': {e}")
    return None


def process_items(items):
    """Process items, catching different exceptions per item."""
    results = []
    for item in items:
        try:
            results.append(100 / int(item))
        except (ValueError, ZeroDivisionError) as e:
            print(f"Skipping {item!r}: {type(e).__name__}: {e}")
    return results


def handle_os_errors(path):
    """Demonstrate OS error hierarchy."""
    try:
        open(path).read()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except PermissionError:
        print(f"Permission denied: {path}")
    except OSError as e:
        print(f"OS error: {e}")


if __name__ == "__main__":
    cfg = {"port": "abc", "debug": "1"}
    print(f"port = {read_setting(cfg, 'port')}")
    print(f"debug = {read_setting(cfg, 'debug')}")
    print(f"host = {read_setting(cfg, 'host', str)}")
    print(f"results = {process_items(['5', '0', 'x', '2'])}")
    handle_os_errors("/no/such/file.txt")
