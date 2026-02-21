"""UserDict for creating custom dictionary subclasses."""

from collections import UserDict


class ReadOnlyDict(UserDict):
    """A dictionary that prevents modification after creation."""

    def __setitem__(self, key, value):
        if self.data:
            raise TypeError("ReadOnlyDict does not support item assignment")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        raise TypeError("ReadOnlyDict does not support item deletion")


class TypedDict(UserDict):
    """A dictionary that enforces value types."""

    def __init__(self, value_type, *args, **kwargs):
        self._value_type = value_type
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(value, self._value_type):
            raise TypeError(f"Value must be {self._value_type.__name__}, got {type(value).__name__}")
        super().__setitem__(key, value)


if __name__ == "__main__":
    # ReadOnlyDict
    ro = ReadOnlyDict({"a": 1, "b": 2})
    print("ReadOnlyDict:", ro)
    print("Access 'a':", ro["a"])
    try:
        ro["c"] = 3
    except TypeError as e:
        print(f"Modification blocked: {e}")

    # TypedDict
    td = TypedDict(int)
    td["x"] = 10
    td["y"] = 20
    print(f"\nTypedDict: {td}")
    try:
        td["z"] = "not an int"
    except TypeError as e:
        print(f"Type error: {e}")
