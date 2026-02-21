"""State machine pattern: change behavior based on internal state."""


class TrafficLight:
    """A traffic light that cycles through states."""

    _transitions = {
        "green": ("yellow", 5),
        "yellow": ("red", 2),
        "red": ("green", 7),
    }

    def __init__(self):
        self.state = "red"

    def next(self):
        """Advance to the next state, return duration of new state."""
        next_state, duration = self._transitions[self.state]
        self.state = next_state
        return duration

    def display(self):
        """Return a visual representation of current state."""
        symbols = {"red": "[R]   ", "yellow": "  [Y] ", "green": "    [G]"}
        return f"{symbols[self.state]} ({self.state})"


def demonstrate_state_machine():
    """Cycle a traffic light through several transitions."""
    light = TrafficLight()
    for _ in range(7):
        duration = light.next()
        print(f"{light.display()} - hold {duration}s")


if __name__ == "__main__":
    demonstrate_state_machine()
