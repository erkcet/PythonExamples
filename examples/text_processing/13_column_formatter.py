"""Format data into aligned columns for display."""


def format_columns(data, headers=None, sep=" | "):
    """Format a list of rows into aligned columns."""
    all_rows = [headers] + data if headers else data
    col_widths = []
    for col in range(len(all_rows[0])):
        max_w = max(len(str(row[col])) for row in all_rows)
        col_widths.append(max_w)
    lines = []
    for i, row in enumerate(all_rows):
        parts = [str(val).ljust(col_widths[j]) for j, val in enumerate(row)]
        lines.append(sep.join(parts))
        if headers and i == 0:
            lines.append(sep.join("-" * w for w in col_widths))
    return "\n".join(lines)


if __name__ == "__main__":
    headers = ["Name", "Age", "City"]
    data = [
        ["Alice", "30", "New York"],
        ["Bob", "25", "San Francisco"],
        ["Charlie", "35", "Chicago"],
    ]
    print(format_columns(data, headers))
