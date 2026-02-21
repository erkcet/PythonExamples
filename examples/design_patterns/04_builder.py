"""Builder pattern: construct complex objects step by step."""


class Pizza:
    """A pizza built with a fluent builder interface."""

    def __init__(self):
        self.size = "medium"
        self.toppings = []
        self.crust = "regular"

    def set_size(self, size):
        self.size = size
        return self

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self

    def set_crust(self, crust):
        self.crust = crust
        return self

    def __str__(self):
        tops = ", ".join(self.toppings) or "plain"
        return f"{self.size} pizza on {self.crust} crust with {tops}"


def build_pizzas():
    """Demonstrate building pizzas with chained calls."""
    margherita = Pizza().set_size("large").set_crust("thin").add_topping("mozzarella").add_topping("basil")
    meat = Pizza().add_topping("pepperoni").add_topping("sausage").set_crust("stuffed")
    print(margherita)
    print(meat)


if __name__ == "__main__":
    build_pizzas()
