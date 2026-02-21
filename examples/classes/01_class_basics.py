"""Basic class definition with __init__, methods, and instances."""


class Dog:
    """A simple Dog class demonstrating basic OOP concepts."""

    species = "Canis familiaris"

    def __init__(self, name, age):
        """Initialize dog with name and age."""
        self.name = name
        self.age = age

    def bark(self):
        """Return a bark string."""
        return f"{self.name} says: Woof!"

    def human_years(self):
        """Approximate age in human years."""
        return self.age * 7

    def description(self):
        """Return a description string."""
        return f"{self.name} is {self.age} years old ({self.species})"


if __name__ == "__main__":
    rex = Dog("Rex", 3)
    luna = Dog("Luna", 5)
    print(rex.bark())
    print(luna.description())
    print(f"{rex.name} in human years: {rex.human_years()}")
    print(f"Same species? {rex.species == luna.species}")
