"""functools.singledispatch for type-based function overloading."""

from functools import singledispatch
from datetime import datetime, date


@singledispatch
def format_value(value):
    """Format a value based on its type (default handler)."""
    return str(value)


@format_value.register(int)
def _format_int(value):
    """Format integers with comma separators."""
    return f"{value:,}"


@format_value.register(float)
def _format_float(value):
    """Format floats to 2 decimal places."""
    return f"{value:,.2f}"


@format_value.register(list)
def _format_list(value):
    """Format lists as bullet points."""
    return "\n".join(f"  - {item}" for item in value)


@format_value.register(dict)
def _format_dict(value):
    """Format dicts as key-value pairs."""
    return "\n".join(f"  {k}: {v}" for k, v in value.items())


@format_value.register(datetime)
@format_value.register(date)
def _format_date(value):
    """Format dates in a readable way."""
    return value.strftime("%B %d, %Y")


if __name__ == "__main__":
    print("int:  ", format_value(1234567))
    print("float:", format_value(3.14159))
    print("str:  ", format_value("hello"))
    print("date: ", format_value(date(2026, 2, 21)))
    print("list:\n" + format_value(["apple", "banana", "cherry"]))
    print("dict:\n" + format_value({"name": "Alice", "age": 30}))

    # Check registered types
    print(f"\nRegistry: {list(format_value.registry.keys())}")
