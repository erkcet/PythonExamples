"""TypedDict for dictionaries with a fixed set of typed keys."""

from typing import TypedDict


class UserProfile(TypedDict):
    """A user profile with known keys and types."""
    name: str
    age: int
    email: str


class Config(TypedDict, total=False):
    """Config where all keys are optional."""
    debug: bool
    log_level: str
    max_retries: int


def display_user(user: UserProfile) -> str:
    """Format a user profile for display."""
    return f"{user['name']} (age {user['age']}) <{user['email']}>"


def apply_config(base: Config, overrides: Config) -> Config:
    """Merge two config dicts, overrides take precedence."""
    merged = {**base, **overrides}
    return merged  # type: ignore[return-value]


def demonstrate_typed_dicts():
    """Show TypedDict providing structure to dictionaries."""
    alice: UserProfile = {"name": "Alice", "age": 30, "email": "a@b.com"}
    print(display_user(alice))

    defaults: Config = {"debug": False, "log_level": "WARNING"}
    custom: Config = {"debug": True, "max_retries": 5}
    final = apply_config(defaults, custom)
    print(f"Config: {final}")


if __name__ == "__main__":
    demonstrate_typed_dicts()
