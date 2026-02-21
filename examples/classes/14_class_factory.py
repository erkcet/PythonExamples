"""Dynamic class creation using type() and class factories."""


def make_dataclass(name, fields):
    """Create a simple data class dynamically with type()."""

    def init(self, *args):
        for field, value in zip(fields, args):
            setattr(self, field, value)

    def repr_(self):
        vals = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
        return f"{name}({vals})"

    def eq(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return all(getattr(self, f) == getattr(other, f) for f in fields)

    cls = type(name, (), {"__init__": init, "__repr__": repr_, "__eq__": eq})
    return cls


def enum_factory(name, values):
    """Create a simple enum-like class from a list of names."""
    namespace = {v: i for i, v in enumerate(values)}
    namespace["_values"] = values
    return type(name, (), namespace)


if __name__ == "__main__":
    Point = make_dataclass("Point", ["x", "y"])
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    print(f"Point: {p1}")
    print(f"Equal: {p1 == p2}")

    Color = enum_factory("Color", ["RED", "GREEN", "BLUE"])
    print(f"RED={Color.RED}, GREEN={Color.GREEN}, BLUE={Color.BLUE}")
    print(f"Values: {Color._values}")
