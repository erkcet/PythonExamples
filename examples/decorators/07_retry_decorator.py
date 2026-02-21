"""Retry decorator: automatically retry a function on failure."""

import time
import random
from functools import wraps


def retry(max_attempts=3, delay=0.1):
    """Decorator factory: retry a function up to max_attempts times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_error
        return wrapper
    return decorator


@retry(max_attempts=5, delay=0.05)
def unreliable_operation():
    """Simulate an operation that fails randomly."""
    if random.random() < 0.6:
        raise ConnectionError("Service unavailable")
    return "Success!"


if __name__ == "__main__":
    random.seed(42)
    try:
        result = unreliable_operation()
        print(f"Result: {result}")
    except ConnectionError as e:
        print(f"All attempts failed: {e}")
