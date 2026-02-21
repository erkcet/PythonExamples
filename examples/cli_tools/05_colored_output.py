"""ANSI colored terminal output without external dependencies."""


COLORS = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "bold": "\033[1m",
    "underline": "\033[4m",
}


def colorize(text: str, *styles: str) -> str:
    """Wrap text with ANSI escape codes for the given styles."""
    codes = "".join(COLORS.get(s, "") for s in styles)
    return f"{codes}{text}{COLORS['reset']}"


def print_status(message: str, level: str = "info"):
    """Print a color-coded status message."""
    color_map = {"info": "cyan", "ok": "green", "warn": "yellow", "error": "red"}
    color = color_map.get(level, "reset")
    prefix = colorize(f"[{level.upper():>5}]", "bold", color)
    print(f"{prefix} {message}")


def demonstrate_colors():
    """Show various colored and styled outputs."""
    for name in ("red", "green", "yellow", "blue", "magenta", "cyan"):
        print(colorize(f"  This text is {name}", name))
    print(colorize("  Bold + Underline", "bold", "underline"))
    print()
    for level in ("info", "ok", "warn", "error"):
        print_status(f"This is a {level} message", level)


if __name__ == "__main__":
    demonstrate_colors()
