"""Singleton pattern implementations."""


class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """Example singleton: database connection."""

    def __init__(self, url="sqlite://default.db"):
        self.url = url
        self.connected = True

    def query(self, sql):
        return f"[{self.url}] {sql}"


def singleton(cls):
    """Decorator-based singleton."""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Config:
    def __init__(self):
        self.settings = {}


if __name__ == "__main__":
    db1 = Database("postgres://localhost/app")
    db2 = Database("mysql://other")
    print(f"Same instance: {db1 is db2}")
    print(f"URL: {db2.url}")  # Still the first URL
    c1, c2 = Config(), Config()
    c1.settings["debug"] = True
    print(f"Config singleton: {c1 is c2}, settings: {c2.settings}")
