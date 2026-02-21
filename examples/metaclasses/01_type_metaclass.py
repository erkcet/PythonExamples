"""Understanding type as a metaclass."""


def greet(self):
    return f"Hello, I'm {self.name}"


# Creating a class dynamically using type()
Person = type("Person", (), {"species": "human", "greet": greet})


def demonstrate_type():
    """Show how type() works as a metaclass."""
    p = Person()
    p.name = "Alice"
    return {
        "class": Person,
        "type_of_class": type(Person),
        "type_of_instance": type(p),
        "greeting": p.greet(),
        "species": p.species,
    }


# Creating with inheritance
Animal = type("Animal", (), {"kingdom": "Animalia"})
Dog = type("Dog", (Animal,), {"speak": lambda self: "Woof!"})


if __name__ == "__main__":
    info = demonstrate_type()
    for k, v in info.items():
        print(f"  {k}: {v}")
    print(f"\nDynamic Dog:")
    d = Dog()
    print(f"  speaks: {d.speak()}")
    print(f"  kingdom: {d.kingdom}")
    print(f"  MRO: {[c.__name__ for c in Dog.__mro__]}")
    print(f"\n  type(int): {type(int)}")
    print(f"  type(type): {type(type)}")
