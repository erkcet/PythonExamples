"""Magic methods: __str__, __repr__, __eq__, __len__, __bool__."""


class Playlist:
    """A music playlist demonstrating common magic methods."""

    def __init__(self, name, songs=None):
        self.name = name
        self.songs = list(songs or [])

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self.songs)} songs)"

    def __repr__(self):
        return f"Playlist({self.name!r}, {self.songs!r})"

    def __len__(self):
        return len(self.songs)

    def __bool__(self):
        return len(self.songs) > 0

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.name == other.name and self.songs == other.songs

    def __contains__(self, song):
        return song in self.songs

    def __getitem__(self, index):
        return self.songs[index]


if __name__ == "__main__":
    p = Playlist("Road Trip", ["Song A", "Song B", "Song C"])
    print(str(p))
    print(repr(p))
    print(f"Length: {len(p)}")
    print(f"Truthy: {bool(p)}")
    print(f"Empty truthy: {bool(Playlist('Empty'))}")
    print(f"'Song B' in playlist: {'Song B' in p}")
    print(f"First song: {p[0]}")
