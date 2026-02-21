"""Using the warnings module for non-fatal alerts."""

import warnings


def calculate_average(values):
    """Calculate average, warning on empty list."""
    if not values:
        warnings.warn("Empty list, returning 0", UserWarning)
        return 0
    return sum(values) / len(values)


def deprecated_function():
    """A function marked as deprecated."""
    warnings.warn(
        "deprecated_function() is deprecated, use new_function()",
        DeprecationWarning,
        stacklevel=2,
    )
    return "old result"


def check_threshold(value, limit=100):
    """Warn if value approaches the limit."""
    if value > limit * 0.9:
        warnings.warn(
            f"Value {value} is near limit {limit}",
            ResourceWarning,
        )
    return value


if __name__ == "__main__":
    warnings.simplefilter("always")
    print(f"Average of []: {calculate_average([])}")
    print(f"Average of [1,2,3]: {calculate_average([1, 2, 3])}")
    print(f"Deprecated: {deprecated_function()}")
    check_threshold(95)
    print("Done")
