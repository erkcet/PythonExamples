"""Convert camelCase or PascalCase strings to snake_case."""


def camel_to_snake(name):
    """Convert camelCase to snake_case."""
    result = [name[0].lower()]
    for ch in name[1:]:
        if ch.isupper():
            result.append('_')
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)


if __name__ == "__main__":
    names = [
        "camelCase",
        "PascalCase",
        "getHTTPResponse",
        "myVariableName",
        "XMLParser",
    ]
    for name in names:
        print(f"{name:25s} -> {camel_to_snake(name)}")
