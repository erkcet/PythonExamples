"""functools.total_ordering to auto-generate comparison methods."""

from functools import total_ordering


@total_ordering
class Temperature:
    """Temperature class with full comparison support."""

    def __init__(self, value, unit="C"):
        self._celsius = value if unit == "C" else (value - 32) * 5 / 9

    @property
    def celsius(self):
        return round(self._celsius, 2)

    @property
    def fahrenheit(self):
        return round(self._celsius * 9 / 5 + 32, 2)

    def __eq__(self, other):
        return self._celsius == other._celsius

    def __lt__(self, other):
        return self._celsius < other._celsius

    def __repr__(self):
        return f"Temperature({self.celsius}C / {self.fahrenheit}F)"


@total_ordering
class Version:
    """Software version with natural ordering."""

    def __init__(self, version_str):
        self.parts = tuple(int(x) for x in version_str.split("."))

    def __eq__(self, other):
        return self.parts == other.parts

    def __lt__(self, other):
        return self.parts < other.parts

    def __repr__(self):
        return f"v{'.'.join(map(str, self.parts))}"


if __name__ == "__main__":
    t1, t2, t3 = Temperature(100), Temperature(212, "F"), Temperature(0)
    print(f"t1: {t1}, t2: {t2}, t3: {t3}")
    print(f"t1 == t2: {t1 == t2}")
    print(f"t3 <= t1: {t3 <= t1}")
    print(f"Sorted: {sorted([t1, t3, t2])}")

    versions = [Version("2.1.0"), Version("1.9.5"), Version("2.0.1")]
    print(f"\nVersions sorted: {sorted(versions)}")
    print(f"v2.1.0 > v1.9.5: {Version('2.1.0') > Version('1.9.5')}")
