"""Function dispatch using functools.singledispatch."""

from functools import singledispatch


@singledispatch
def process(value):
    """Default handler for unsupported types."""
    raise TypeError(f"Unsupported type: {type(value)}")


@process.register(int)
def _process_int(value):
    """Handle integer values."""
    return f"Integer: {value * 2}"


@process.register(str)
def _process_str(value):
    """Handle string values."""
    return f"String: {value.upper()}"


@process.register(list)
def _process_list(value):
    """Handle list values."""
    return f"List of {len(value)} items: {value}"


@process.register(float)
def _process_float(value):
    """Handle float values."""
    return f"Float rounded: {round(value, 2)}"


if __name__ == "__main__":
    print(process(42))
    print(process("hello"))
    print(process([1, 2, 3]))
    print(process(3.14159))
    try:
        process({})
    except TypeError as e:
        print(f"Caught: {e}")
