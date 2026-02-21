"""Simple rate limiter using token bucket algorithm."""

import time
import threading


class RateLimiter:
    """Token bucket rate limiter."""

    def __init__(self, rate, burst=None):
        self.rate = rate
        self.burst = burst or rate
        self.tokens = self.burst
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self.last_refill
        self.tokens = min(self.burst, self.tokens + elapsed * self.rate)
        self.last_refill = now

    def acquire(self, tokens=1):
        """Try to acquire tokens. Returns True if allowed."""
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def wait(self, tokens=1):
        """Block until tokens are available."""
        while not self.acquire(tokens):
            time.sleep(0.01)


if __name__ == "__main__":
    limiter = RateLimiter(rate=5, burst=5)
    print("Rate limiter (5/sec, burst=5):")
    for i in range(8):
        allowed = limiter.acquire()
        print(f"  Request {i+1}: {'allowed' if allowed else 'denied'}")
    print("\nWaiting for refill...")
    time.sleep(0.5)
    print(f"  After 0.5s: {'allowed' if limiter.acquire() else 'denied'}")
