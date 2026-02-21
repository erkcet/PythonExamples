"""Dataclass inheritance patterns."""

from dataclasses import dataclass, field


@dataclass
class Animal:
    """Base animal class."""
    name: str
    species: str
    sound: str = "..."

    def speak(self):
        return f"{self.name} says {self.sound}!"


@dataclass
class Pet(Animal):
    """Pet with an owner."""
    owner: str = ""
    vaccinated: bool = False

    def info(self):
        status = "vaccinated" if self.vaccinated else "not vaccinated"
        return f"{self.name} ({self.species}), owner: {self.owner}, {status}"


@dataclass
class Dog(Pet):
    """Dog with breed information."""
    breed: str = "Mixed"
    sound: str = "Woof"

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"


if __name__ == "__main__":
    dog = Dog("Rex", "Canine", owner="Alice", breed="Labrador", vaccinated=True)
    print(dog)
    print(dog.speak())
    print(dog.info())
    print(dog.fetch("ball"))
    cat = Pet("Whiskers", "Feline", "Meow", "Bob", True)
    print(f"\n{cat}")
    print(cat.speak())
