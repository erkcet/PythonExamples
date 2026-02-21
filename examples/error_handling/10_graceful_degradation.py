"""Graceful error recovery patterns."""


def with_retry(func, retries=3, default=None):
    """Retry a function up to N times before returning default."""
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            last_error = e
            print(f"  Attempt {attempt} failed: {e}")
    print(f"  All {retries} attempts failed, using default={default}")
    return default


_call_count = 0


def flaky_function():
    """Succeeds only on the 3rd call."""
    global _call_count
    _call_count += 1
    if _call_count < 3:
        raise ConnectionError("Server busy")
    return "success"


def get_with_fallback(*sources):
    """Try multiple sources, return first success."""
    for source in sources:
        try:
            return source()
        except Exception as e:
            print(f"  Source failed: {e}")
    return None


if __name__ == "__main__":
    print("=== Retry pattern ===")
    result = with_retry(flaky_function)
    print(f"Result: {result}")

    print("\n=== Fallback pattern ===")
    def bad(): raise ValueError("unavailable")
    def good(): return 42
    result = get_with_fallback(bad, bad, good)
    print(f"Fallback result: {result}")
