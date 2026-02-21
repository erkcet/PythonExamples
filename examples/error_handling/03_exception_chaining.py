"""Exception chaining with 'from' keyword."""


class ConfigError(Exception):
    """Raised when configuration loading fails."""


def parse_port(value):
    """Parse a port number from string."""
    try:
        port = int(value)
    except ValueError as e:
        raise ConfigError(f"Invalid port: {value!r}") from e
    if not 1 <= port <= 65535:
        raise ConfigError(f"Port out of range: {port}")
    return port


def load_config(data):
    """Load configuration from a dict."""
    try:
        return {"port": parse_port(data.get("port", "8080"))}
    except ConfigError as e:
        raise RuntimeError("Failed to load configuration") from e


if __name__ == "__main__":
    try:
        load_config({"port": "abc"})
    except RuntimeError as e:
        print(f"Error: {e}")
        print(f"Caused by: {e.__cause__}")
        print(f"Root cause: {e.__cause__.__cause__}")

    # Suppress chaining with 'from None'
    try:
        int("bad")
    except ValueError:
        raise SystemExit("Fatal: bad input") from None
