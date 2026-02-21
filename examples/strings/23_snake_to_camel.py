"""Convert snake_case strings to camelCase and PascalCase."""


def snake_to_camel(name):
    """Convert snake_case to camelCase."""
    parts = name.split('_')
    return parts[0] + ''.join(w.capitalize() for w in parts[1:])


def snake_to_pascal(name):
    """Convert snake_case to PascalCase."""
    return ''.join(w.capitalize() for w in name.split('_'))


if __name__ == "__main__":
    names = [
        "my_variable_name",
        "get_http_response",
        "hello_world",
        "single",
    ]
    for name in names:
        print(f"{name:25s} -> camel: {snake_to_camel(name):25s} pascal: {snake_to_pascal(name)}")
