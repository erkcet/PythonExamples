"""ABC and abstract methods for enforcing interfaces."""

from abc import ABC, abstractmethod


class Serializable(ABC):
    """Abstract base class requiring serialize and deserialize."""

    @abstractmethod
    def serialize(self):
        """Convert object to a string representation."""
        ...

    @classmethod
    @abstractmethod
    def deserialize(cls, data):
        """Create an instance from a string representation."""
        ...


class User(Serializable):
    """Concrete class implementing Serializable."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def serialize(self):
        return f"{self.name},{self.age}"

    @classmethod
    def deserialize(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

    def __repr__(self):
        return f"User({self.name!r}, {self.age})"


if __name__ == "__main__":
    user = User("Alice", 30)
    data = user.serialize()
    print(f"Serialized: {data}")
    restored = User.deserialize(data)
    print(f"Restored: {restored}")
    print(f"Is Serializable? {isinstance(user, Serializable)}")
    try:
        Serializable()
    except TypeError as e:
        print(f"Cannot instantiate ABC: {e}")
