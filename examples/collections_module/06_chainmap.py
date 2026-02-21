"""ChainMap usage for combining multiple mappings."""

from collections import ChainMap


def merge_configs(*configs):
    """Merge multiple configuration dicts with priority (first wins)."""
    return ChainMap(*configs)


def scoped_variables():
    """Simulate variable scoping with ChainMap."""
    global_scope = {"x": 1, "y": 2, "z": 3}
    local_scope = {"x": 10, "w": 40}
    return ChainMap(local_scope, global_scope)


if __name__ == "__main__":
    defaults = {"color": "blue", "size": "medium", "verbose": False}
    user_prefs = {"color": "red", "verbose": True}
    cli_args = {"verbose": False}

    config = merge_configs(cli_args, user_prefs, defaults)
    print("Merged config:")
    for key in ["color", "size", "verbose"]:
        print(f"  {key}: {config[key]}")

    print(f"\nAll keys: {list(config.keys())}")
    print(f"Maps: {config.maps}")

    scope = scoped_variables()
    print(f"\nScoped x: {scope['x']} (local overrides global)")
    print(f"Scoped y: {scope['y']} (from global)")

    # New child scope
    inner = scope.new_child({"x": 100})
    print(f"Inner x: {inner['x']}, parents x: {inner.parents['x']}")
