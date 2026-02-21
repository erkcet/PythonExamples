"""Class attributes vs instance attributes."""


class Counter:
    """Demonstrates class vs instance attribute behavior."""

    total_instances = 0  # class attribute shared by all

    def __init__(self, name):
        self.name = name         # instance attribute
        self.count = 0           # instance attribute
        Counter.total_instances += 1

    def increment(self):
        """Increment this instance's count."""
        self.count += 1

    @classmethod
    def get_total_instances(cls):
        """Return the total number of instances created."""
        return cls.total_instances


class Config:
    """Config with class-level defaults and instance overrides."""

    debug = False
    verbose = True

    def __init__(self, **overrides):
        for key, val in overrides.items():
            setattr(self, key, val)


if __name__ == "__main__":
    a = Counter("A")
    b = Counter("B")
    a.increment()
    a.increment()
    b.increment()
    print(f"A count: {a.count}, B count: {b.count}")
    print(f"Total instances: {Counter.get_total_instances()}")

    c1 = Config()
    c2 = Config(debug=True)
    print(f"c1.debug={c1.debug}, c2.debug={c2.debug}")
    print(f"Class default: Config.debug={Config.debug}")
