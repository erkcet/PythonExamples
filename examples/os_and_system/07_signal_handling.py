"""Basic signal handling concepts."""

import signal
import sys
import os


def setup_graceful_shutdown(cleanup_fn):
    """Register a cleanup function for SIGTERM/SIGINT."""
    def handler(signum, frame):
        name = signal.Signals(signum).name
        print(f"\n  Received {name}, cleaning up...")
        cleanup_fn()
        sys.exit(0)
    signal.signal(signal.SIGTERM, handler)
    signal.signal(signal.SIGINT, handler)


def list_signals():
    """List available signals on this platform."""
    return {s.name: s.value for s in signal.Signals}


def demo_alarm():
    """Demonstrate SIGALRM (Unix only)."""
    if not hasattr(signal, "SIGALRM"):
        return "SIGALRM not available on this platform"
    def handler(signum, frame):
        print("  Alarm triggered!")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    return "Alarm set for 1 second"


if __name__ == "__main__":
    print("Available signals:")
    for name, val in sorted(list_signals().items(), key=lambda x: x[1])[:10]:
        print(f"  {name}: {val}")
    print(f"\nPID: {os.getpid()}")
    setup_graceful_shutdown(lambda: print("  Resources cleaned up"))
    print("Signal handlers registered. Press Ctrl+C to test (or run normally).")
