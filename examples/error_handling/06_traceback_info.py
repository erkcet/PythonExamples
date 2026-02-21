"""Working with traceback information."""

import traceback
import sys


def faulty_function():
    """A function that raises an error."""
    return 1 / 0


def capture_traceback():
    """Capture and inspect traceback details."""
    try:
        faulty_function()
    except ZeroDivisionError:
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"Exception type: {exc_type.__name__}")
        print(f"Exception value: {exc_value}")
        tb_lines = traceback.format_tb(exc_tb)
        print(f"Traceback depth: {len(tb_lines)}")
        for line in tb_lines:
            print(line, end="")


def format_exception_string():
    """Format an exception as a string for logging."""
    try:
        faulty_function()
    except ZeroDivisionError:
        error_str = traceback.format_exc()
        print("Formatted exception:")
        print(error_str)


def extract_tb_details():
    """Extract structured traceback info."""
    try:
        faulty_function()
    except ZeroDivisionError:
        tb = traceback.extract_tb(sys.exc_info()[2])
        for frame in tb:
            print(f"  File {frame.filename}, line {frame.lineno}, "
                  f"in {frame.name}: {frame.line}")


if __name__ == "__main__":
    capture_traceback()
    print("-" * 40)
    format_exception_string()
    print("-" * 40)
    extract_tb_details()
