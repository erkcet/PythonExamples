"""MRO (Method Resolution Order) and super() in diamond inheritance."""


class A:
    """Base class A."""

    def greet(self):
        return "Hello from A"

    def who(self):
        return ["A"]


class B(A):
    """Class B inherits from A."""

    def greet(self):
        return "Hello from B"

    def who(self):
        return ["B"] + super().who()


class C(A):
    """Class C inherits from A."""

    def greet(self):
        return "Hello from C"

    def who(self):
        return ["C"] + super().who()


class D(B, C):
    """Class D: diamond inheritance from B and C."""

    def greet(self):
        return "Hello from D"

    def who(self):
        return ["D"] + super().who()


if __name__ == "__main__":
    d = D()
    print(f"Greet: {d.greet()}")
    print(f"Who chain: {d.who()}")
    print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")

    # super() follows MRO, not the direct parent
    c = C()
    print(f"C.who: {c.who()}")
    print(f"C MRO: {[cls.__name__ for cls in C.__mro__]}")
