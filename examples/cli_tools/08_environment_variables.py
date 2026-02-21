"""Working with environment variables using os.environ."""

import os


def get_env(name: str, default: str = "") -> str:
    """Get an environment variable with a fallback default."""
    return os.environ.get(name, default)


def require_env(name: str) -> str:
    """Get a required env var, raising if missing."""
    value = os.environ.get(name)
    if value is None:
        raise EnvironmentError(f"Missing required env var: {name}")
    return value


def show_common_env_vars():
    """Display common environment variables."""
    common = ["HOME", "USER", "SHELL", "PATH", "LANG", "TERM"]
    for var in common:
        value = get_env(var, "(not set)")
        if var == "PATH":
            value = value[:60] + "..." if len(value) > 60 else value
        print(f"  {var:>8} = {value}")


def demonstrate_env_vars():
    """Show reading, setting, and checking env vars."""
    print("Common environment variables:")
    show_common_env_vars()

    print("\nSetting MY_APP_MODE=production")
    os.environ["MY_APP_MODE"] = "production"
    print(f"  MY_APP_MODE = {get_env('MY_APP_MODE')}")

    print(f"\nDefault value: {get_env('NONEXISTENT', 'fallback')}")
    del os.environ["MY_APP_MODE"]


if __name__ == "__main__":
    demonstrate_env_vars()
