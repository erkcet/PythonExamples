"""Wrap text with various options: indent, hanging indent, prefix."""

import textwrap


def wrap_with_options(text, width=50, indent="", hang="", prefix=""):
    """Wrap text with configurable indent, hanging indent, and prefix."""
    lines = textwrap.fill(
        text, width=width,
        initial_indent=indent + prefix,
        subsequent_indent=hang + prefix
    )
    return lines


if __name__ == "__main__":
    text = ("The quick brown fox jumps over the lazy dog. "
            "Pack my box with five dozen liquor jugs. "
            "How vexingly quick daft zebras jump.")
    print("Basic wrap (40 chars):")
    print(wrap_with_options(text, width=40))
    print("\nWith bullet prefix:")
    print(wrap_with_options(text, width=40, indent="* ", hang="  "))
    print("\nWith line prefix:")
    print(wrap_with_options(text, width=40, prefix="> "))
