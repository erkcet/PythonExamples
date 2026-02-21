"""Working with environment variables using os.environ."""

import os


def get_env(key, default=None):
    """Get an environment variable with optional default."""
    return os.environ.get(key, default)


def set_env(key, value):
    """Set an environment variable for the current process."""
    os.environ[key] = value


def list_env_vars(prefix=None):
    """List environment variables, optionally filtered by prefix."""
    items = os.environ.items()
    if prefix:
        items = [(k, v) for k, v in items if k.startswith(prefix)]
    return dict(items)


def env_summary():
    """Get a summary of the environment."""
    return {
        "HOME": get_env("HOME", "not set"),
        "PATH_entries": len(get_env("PATH", "").split(os.pathsep)),
        "SHELL": get_env("SHELL", "not set"),
        "USER": get_env("USER", "not set"),
        "total_vars": len(os.environ),
    }


if __name__ == "__main__":
    print("Environment summary:", env_summary())
    set_env("MY_APP_DEBUG", "true")
    print(f"MY_APP_DEBUG = {get_env('MY_APP_DEBUG')}")
    print(f"Vars starting with 'MY_': {list_env_vars('MY_')}")
