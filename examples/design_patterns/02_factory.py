"""Factory pattern: create objects without specifying exact classes."""


class Dog:
    """A dog that speaks."""
    def speak(self):
        return "Woof!"


class Cat:
    """A cat that speaks."""
    def speak(self):
        return "Meow!"


class Fish:
    """A fish that speaks."""
    def speak(self):
        return "Blub!"


def animal_factory(animal_type: str):
    """Create an animal based on the given type string."""
    animals = {"dog": Dog, "cat": Cat, "fish": Fish}
    creator = animals.get(animal_type.lower())
    if creator is None:
        raise ValueError(f"Unknown animal type: {animal_type}")
    return creator()


def demonstrate_factory():
    """Show factory creating different objects from strings."""
    for name in ("dog", "cat", "fish"):
        animal = animal_factory(name)
        print(f"{name}: {animal.speak()}")


if __name__ == "__main__":
    demonstrate_factory()
