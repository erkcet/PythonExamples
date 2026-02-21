"""Center text within a given width using a fill character."""


def center_text(text, width, fill=' '):
    """Center text within the given width."""
    if len(text) >= width:
        return text
    total_padding = width - len(text)
    left = total_padding // 2
    right = total_padding - left
    return fill * left + text + fill * right


def create_banner(text, width=40, border='*'):
    """Create a banner box around text."""
    lines = [border * width]
    lines.append(center_text(text, width - 2, ' ').join([border, border]))
    lines.append(border * width)
    return '\n'.join(lines)


if __name__ == "__main__":
    print(center_text("Hello", 20, '-'))
    print(center_text("Python", 20, '='))
    print()
    print(create_banner("Welcome to Python"))
