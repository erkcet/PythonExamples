"""Descriptor protocol: __get__, __set__, __delete__."""


class Validated:
    """Descriptor that validates values with a custom check."""

    def __init__(self, validator, message="Invalid value"):
        self.validator = validator
        self.message = message

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"{self.message}: {value!r}")
        setattr(obj, self.name, value)


class PositiveInt(Validated):
    """Descriptor for positive integers."""

    def __init__(self):
        super().__init__(
            lambda v: isinstance(v, int) and v > 0,
            "Must be a positive integer",
        )


class Product:
    """Product with validated attributes."""

    name = Validated(lambda v: isinstance(v, str) and len(v) > 0, "Name required")
    price = PositiveInt()
    quantity = PositiveInt()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


if __name__ == "__main__":
    p = Product("Widget", 10, 5)
    print(f"{p.name}: ${p.price} x {p.quantity} = ${p.total()}")
    try:
        p.price = -1
    except ValueError as e:
        print(f"Validation: {e}")
