"""Simple file locking patterns using lock files."""

import os
import time
import tempfile


class FileLock:
    """A simple file-based lock using a .lock file."""

    def __init__(self, path):
        self.lock_path = path + ".lock"
        self.fd = None

    def acquire(self, timeout=5):
        """Acquire the lock, waiting up to timeout seconds."""
        start = time.time()
        while True:
            try:
                self.fd = os.open(self.lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                print(f"Lock acquired: {self.lock_path}")
                return True
            except FileExistsError:
                if time.time() - start > timeout:
                    raise TimeoutError("Could not acquire lock")
                time.sleep(0.1)

    def release(self):
        """Release the lock."""
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
        os.remove(self.lock_path)
        print(f"Lock released: {self.lock_path}")

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *exc):
        self.release()
        return False


if __name__ == "__main__":
    filepath = os.path.join(tempfile.gettempdir(), "shared_resource.txt")
    with FileLock(filepath) as lock:
        with open(filepath, "w") as f:
            f.write("protected write\n")
        print(f"Wrote to {filepath} under lock")
    print("Lock released, operation complete")
    os.remove(filepath)
