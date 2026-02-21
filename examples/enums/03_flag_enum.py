"""Flag and IntFlag for bitwise enum combinations."""

from enum import Flag, IntFlag, auto


class Permission(Flag):
    """File permissions as flags."""
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

    @classmethod
    def all(cls):
        return cls.READ | cls.WRITE | cls.EXECUTE


class Style(IntFlag):
    """Text style flags (combinable)."""
    BOLD = 1
    ITALIC = 2
    UNDERLINE = 4
    STRIKETHROUGH = 8

    def describe(self):
        return " + ".join(s.name for s in Style if s in self)


if __name__ == "__main__":
    perm = Permission.READ | Permission.WRITE
    print(f"Permissions: {perm}")
    print(f"Has READ: {Permission.READ in perm}")
    print(f"Has EXECUTE: {Permission.EXECUTE in perm}")
    print(f"All: {Permission.all()}")
    style = Style.BOLD | Style.ITALIC
    print(f"\nStyle: {style}")
    print(f"Description: {style.describe()}")
    print(f"Value: {style.value}")
    full = Style.BOLD | Style.ITALIC | Style.UNDERLINE
    print(f"Full style: {full.describe()}")
