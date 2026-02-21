"""Retry with exponential backoff decorator."""

import time
import random
import functools


def retry(max_attempts=3, base_delay=1.0, backoff_factor=2.0, jitter=True):
    """Decorator to retry a function with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    delay = base_delay * (backoff_factor ** attempt)
                    if jitter:
                        delay *= random.uniform(0.5, 1.5)
                    print(f"  Attempt {attempt+1} failed: {e}. Retrying in {delay:.2f}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


call_count = 0

@retry(max_attempts=3, base_delay=0.1, jitter=False)
def flaky_function():
    """Simulates a function that fails twice then succeeds."""
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError(f"Attempt {call_count} failed")
    return "Success!"


if __name__ == "__main__":
    call_count = 0
    result = flaky_function()
    print(f"Result: {result} (took {call_count} attempts)")
