"""Singleton pattern via metaclass."""


class SingletonMeta(type):
    """Metaclass ensuring only one instance per class."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    def reset(cls):
        """Allow resetting the singleton (useful for testing)."""
        cls._instances.pop(cls, None)


class AppConfig(metaclass=SingletonMeta):
    """Application configuration singleton."""

    def __init__(self):
        self.settings = {"debug": False, "log_level": "INFO"}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)


class Logger(metaclass=SingletonMeta):
    """Logger singleton."""

    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)


if __name__ == "__main__":
    c1 = AppConfig()
    c1.set("debug", True)
    c2 = AppConfig()
    print(f"Same instance: {c1 is c2}")
    print(f"debug from c2: {c2.get('debug')}")
    l1 = Logger()
    l1.log("started")
    l2 = Logger()
    print(f"Logger singleton: {l1 is l2}, logs: {l2.logs}")
    print(f"Different singletons: {c1 is not l1}")
