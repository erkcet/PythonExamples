"""Singleton pattern: ensure only one instance exists."""


class SingletonMeta(type):
    """Metaclass that enforces the singleton pattern."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """A database connection that should only exist once."""

    def __init__(self, host="localhost"):
        self.host = host
        self.connected = True

    def query(self, sql):
        """Simulate a database query."""
        return f"Executed on {self.host}: {sql}"


class AppConfig(metaclass=SingletonMeta):
    """Application config as a singleton."""

    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value


if __name__ == "__main__":
    db1 = Database("prod-server")
    db2 = Database("other-server")
    print(f"Same instance: {db1 is db2}")
    print(f"Host: {db2.host}")
    print(db1.query("SELECT 1"))

    cfg1 = AppConfig()
    cfg1.set("debug", True)
    cfg2 = AppConfig()
    print(f"Config same: {cfg1 is cfg2}")
    print(f"Settings: {cfg2.settings}")
