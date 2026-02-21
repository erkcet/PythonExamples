"""Text table formatting without external dependencies."""


def format_table(headers: list[str], rows: list[list], align: str = "<") -> str:
    """Format data as an aligned text table with borders."""
    all_rows = [headers] + [[str(c) for c in r] for r in rows]
    widths = [max(len(r[i]) for r in all_rows) for i in range(len(headers))]
    sep = "+-" + "-+-".join("-" * w for w in widths) + "-+"

    def fmt_row(row):
        cells = [f"{row[i]:{align}{widths[i]}}" for i in range(len(row))]
        return "| " + " | ".join(cells) + " |"

    lines = [sep, fmt_row(headers), sep]
    for row in all_rows[1:]:
        lines.append(fmt_row(row))
    lines.append(sep)
    return "\n".join(lines)


def demonstrate_table():
    """Print a formatted table of sample data."""
    headers = ["Name", "Language", "Stars"]
    rows = [
        ["Flask", "Python", 65000],
        ["Express", "JavaScript", 62000],
        ["Rails", "Ruby", 54000],
        ["Gin", "Go", 73000],
    ]
    print(format_table(headers, rows))


if __name__ == "__main__":
    demonstrate_table()
