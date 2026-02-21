"""Enforce abstract methods using a metaclass."""


class AbstractMeta(type):
    """Metaclass that enforces implementation of required methods."""

    def __new__(mcs, name, bases, namespace, required=None, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        if required is not None:
            cls._required_methods = required
        elif not hasattr(cls, "_required_methods"):
            cls._required_methods = []
        # Check concrete classes (those with a base using this metaclass)
        for base in bases:
            if hasattr(base, "_required_methods"):
                for method in base._required_methods:
                    if method not in namespace:
                        raise TypeError(
                            f"{name} must implement '{method}'"
                        )
        return cls


class Serializer(metaclass=AbstractMeta, required=["serialize", "deserialize"]):
    """Base serializer that requires serialize/deserialize methods."""
    pass


class JSONSerializer(Serializer):
    def serialize(self, data):
        return f"JSON: {data}"

    def deserialize(self, text):
        return f"parsed: {text}"


if __name__ == "__main__":
    js = JSONSerializer()
    print(f"Serialize: {js.serialize({'a': 1})}")
    raw = '{"a": 1}'
    print(f"Deserialize: {js.deserialize(raw)}")
    try:
        # This will fail at class creation time
        exec("""
class IncompleteSerializer(Serializer):
    def serialize(self, data):
        return str(data)
""")
    except TypeError as e:
        print(f"\nEnforcement: {e}")
