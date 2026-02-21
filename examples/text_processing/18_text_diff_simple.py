"""Show a simple line-by-line diff between two texts."""

import difflib


def simple_diff(text1, text2):
    """Return a unified diff between two text strings."""
    lines1 = text1.splitlines(keepends=True)
    lines2 = text2.splitlines(keepends=True)
    diff = difflib.unified_diff(lines1, lines2,
                                fromfile="original", tofile="modified", lineterm="")
    return list(diff)


if __name__ == "__main__":
    original = """def greet(name):
    print("Hello " + name)
    return None

greet("World")"""

    modified = """def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    print(message)
    return message

greet("World", "Hi")"""

    diff_lines = simple_diff(original, modified)
    print("Diff output:")
    for line in diff_lines:
        print(line.rstrip())
