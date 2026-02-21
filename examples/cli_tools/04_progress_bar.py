"""Simple text progress bar using only the standard library."""

import time
import sys


def progress_bar(current: int, total: int, width: int = 40) -> str:
    """Return a formatted progress bar string."""
    fraction = current / total
    filled = int(width * fraction)
    bar = "#" * filled + "-" * (width - filled)
    percent = fraction * 100
    return f"\r[{bar}] {percent:5.1f}% ({current}/{total})"


def run_with_progress(total: int = 50):
    """Simulate a task with a visible progress bar."""
    print("Processing items...")
    for i in range(1, total + 1):
        sys.stdout.write(progress_bar(i, total))
        sys.stdout.flush()
        time.sleep(0.03)
    print("\nDone!")


if __name__ == "__main__":
    run_with_progress()
