"""Bidirectional dictionary mapping."""


class BiDict:
    """A dictionary that maintains forward and reverse mappings."""

    def __init__(self, initial=None):
        self._forward = {}
        self._reverse = {}
        if initial:
            for k, v in initial.items():
                self.put(k, v)

    def put(self, key, value):
        """Set a bidirectional mapping."""
        if key in self._forward:
            del self._reverse[self._forward[key]]
        if value in self._reverse:
            del self._forward[self._reverse[value]]
        self._forward[key] = value
        self._reverse[value] = key

    def get_by_key(self, key, default=None):
        """Look up by forward key."""
        return self._forward.get(key, default)

    def get_by_value(self, value, default=None):
        """Look up by reverse key (value)."""
        return self._reverse.get(value, default)

    def __repr__(self):
        return f"BiDict({self._forward})"

    def __len__(self):
        return len(self._forward)


if __name__ == "__main__":
    codes = BiDict({"US": 1, "UK": 44, "IN": 91, "JP": 81})
    print(f"BiDict: {codes}")
    print(f"US -> {codes.get_by_key('US')}")
    print(f"44 -> {codes.get_by_value(44)}")
    codes.put("FR", 33)
    print(f"After adding FR: {codes}, len={len(codes)}")
