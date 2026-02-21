"""Observer pattern: notify multiple listeners of state changes."""


class EventEmitter:
    """A simple event system that notifies registered listeners."""

    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        """Register a callback for an event."""
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args):
        """Emit an event, calling all registered callbacks."""
        for cb in self._listeners.get(event, []):
            cb(*args)


def demonstrate_observer():
    """Show observers reacting to emitted events."""
    emitter = EventEmitter()
    emitter.on("login", lambda user: print(f"  Logger: {user} logged in"))
    emitter.on("login", lambda user: print(f"  Greeter: Welcome, {user}!"))
    emitter.on("logout", lambda user: print(f"  Logger: {user} logged out"))

    for action, user in [("login", "Alice"), ("login", "Bob"), ("logout", "Alice")]:
        print(f"Event: {action}")
        emitter.emit(action, user)


if __name__ == "__main__":
    demonstrate_observer()
