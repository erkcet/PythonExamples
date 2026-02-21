"""Mixin classes for reusable, composable behavior."""

import json


class JsonMixin:
    """Mixin that adds JSON serialization."""

    def to_json(self):
        """Serialize public attributes to JSON."""
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str):
        """Create instance from JSON string."""
        return cls(**json.loads(json_str))


class ReprMixin:
    """Mixin that auto-generates __repr__ from attributes."""

    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class EqualityMixin:
    """Mixin that adds equality based on __dict__."""

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.__dict__ == other.__dict__


class User(JsonMixin, ReprMixin, EqualityMixin):
    """User class enhanced with mixins."""

    def __init__(self, name, email):
        self.name = name
        self.email = email


if __name__ == "__main__":
    u1 = User("Alice", "alice@example.com")
    print(repr(u1))
    j = u1.to_json()
    print(f"JSON: {j}")
    u2 = User.from_json(j)
    print(f"Equal: {u1 == u2}")
