"""Single and multiple inheritance examples."""


class Animal:
    """Base animal class."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Override in subclass."""
        raise NotImplementedError


class Dog(Animal):
    """Dog inherits from Animal."""

    def speak(self):
        return f"{self.name}: Woof!"


class Cat(Animal):
    """Cat inherits from Animal."""

    def speak(self):
        return f"{self.name}: Meow!"


class Swimmer:
    """Mixin for swimming ability."""

    def swim(self):
        return f"{self.name} is swimming"


class Labrador(Dog, Swimmer):
    """Multiple inheritance: Dog + Swimmer."""

    def fetch(self):
        return f"{self.name} fetches the ball"


if __name__ == "__main__":
    dog = Dog("Rex")
    cat = Cat("Whiskers")
    print(dog.speak())
    print(cat.speak())

    lab = Labrador("Buddy")
    print(lab.speak())
    print(lab.swim())
    print(lab.fetch())
    print(f"Is Animal? {isinstance(lab, Animal)}")
