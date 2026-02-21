"""Using auto() for automatic enum values."""

from enum import Enum, auto


class Season(Enum):
    """Seasons with auto-generated values."""
    SPRING = auto()
    SUMMER = auto()
    AUTUMN = auto()
    WINTER = auto()

    def next(self):
        members = list(type(self))
        idx = (members.index(self) + 1) % len(members)
        return members[idx]


class Planet(Enum):
    """Planets with custom auto values using _generate_next_value_."""
    MERCURY = auto()
    VENUS = auto()
    EARTH = auto()
    MARS = auto()

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class LogLevel(Enum):
    """Log levels with auto values starting from 10."""
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return (count + 1) * 10


if __name__ == "__main__":
    print("Seasons:", [(s.name, s.value) for s in Season])
    print(f"After AUTUMN: {Season.AUTUMN.next()}")
    print(f"\nPlanets: {[(p.name, p.value) for p in Planet]}")
    print(f"Log levels: {[(l.name, l.value) for l in LogLevel]}")
