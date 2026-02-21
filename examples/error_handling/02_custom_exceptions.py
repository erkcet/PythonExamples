"""Define and use custom exception classes."""


class AppError(Exception):
    """Base exception for this application."""


class ValidationError(AppError):
    """Raised when input validation fails."""

    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")


class NotFoundError(AppError):
    """Raised when a resource is not found."""

    def __init__(self, resource, identifier):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} '{identifier}' not found")


def validate_age(age):
    """Validate that age is a positive integer."""
    if not isinstance(age, int) or age < 0:
        raise ValidationError("age", "must be a non-negative integer")
    return age


def find_user(user_id, users):
    """Find a user by ID."""
    if user_id not in users:
        raise NotFoundError("User", user_id)
    return users[user_id]


if __name__ == "__main__":
    try:
        validate_age(-5)
    except ValidationError as e:
        print(f"Validation failed: {e} (field={e.field})")

    try:
        find_user(99, {1: "Alice", 2: "Bob"})
    except NotFoundError as e:
        print(f"Lookup failed: {e}")
