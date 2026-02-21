"""Callback functions: passing functions as arguments."""


def process_items(items, on_item, on_done=None):
    """Process each item via a callback, then call on_done."""
    results = []
    for item in items:
        results.append(on_item(item))
    if on_done:
        on_done(results)
    return results


def event_emitter():
    """Simple event emitter using callback registration."""
    listeners = {}

    def on(event, callback):
        listeners.setdefault(event, []).append(callback)

    def emit(event, *args):
        for cb in listeners.get(event, []):
            cb(*args)

    return on, emit


if __name__ == "__main__":
    results = process_items(
        [1, 2, 3, 4],
        on_item=lambda x: x ** 2,
        on_done=lambda r: print(f"Done! Results: {r}"),
    )

    on, emit = event_emitter()
    on("greet", lambda name: print(f"Hello, {name}!"))
    on("greet", lambda name: print(f"Welcome, {name}!"))
    emit("greet", "Alice")
