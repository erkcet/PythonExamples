"""Simple event emitter (pub/sub) pattern."""


class EventEmitter:
    """Lightweight event emitter for pub/sub communication."""

    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        """Register a callback for an event."""
        self._listeners.setdefault(event, []).append(callback)
        return self

    def off(self, event, callback=None):
        """Remove a callback (or all callbacks) for an event."""
        if callback:
            self._listeners.get(event, []).remove(callback)
        else:
            self._listeners.pop(event, None)

    def emit(self, event, *args, **kwargs):
        """Emit an event, calling all registered callbacks."""
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)

    def once(self, event, callback):
        """Register a callback that fires only once."""
        def wrapper(*args, **kwargs):
            callback(*args, **kwargs)
            self.off(event, wrapper)
        self.on(event, wrapper)


if __name__ == "__main__":
    emitter = EventEmitter()
    emitter.on("data", lambda d: print(f"  Received: {d}"))
    emitter.on("data", lambda d: print(f"  Logged: {d}"))
    emitter.once("connect", lambda: print("  Connected (once)!"))
    print("Emit 'connect':")
    emitter.emit("connect")
    emitter.emit("connect")  # Won't fire again
    print("Emit 'data':")
    emitter.emit("data", {"user": "alice", "action": "login"})
