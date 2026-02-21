"""Simulated database transaction context manager."""


class Database:
    """A simulated in-memory database."""

    def __init__(self):
        self.data = {}
        self._snapshot = None

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def transaction(self):
        return Transaction(self)


class Transaction:
    """Context manager for atomic database operations."""

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.db._snapshot = dict(self.db.data)
        print("Transaction started")
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.db.data = self.db._snapshot
            print(f"Transaction rolled back: {exc_val}")
        else:
            print("Transaction committed")
        self.db._snapshot = None
        return True  # Suppress the exception


if __name__ == "__main__":
    db = Database()
    db.set("balance", 100)

    with db.transaction():
        db.set("balance", 150)
        db.set("name", "Alice")
    print(f"After commit: {db.data}")

    with db.transaction():
        db.set("balance", 9999)
        raise ValueError("Something failed")
    print(f"After rollback: {db.data}")
