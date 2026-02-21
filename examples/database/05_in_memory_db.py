"""In-memory SQLite database for testing and caching."""

import sqlite3


class InMemoryCache:
    """Key-value cache backed by in-memory SQLite."""

    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            "CREATE TABLE cache (key TEXT PRIMARY KEY, value TEXT, hits INTEGER DEFAULT 0)"
        )

    def set(self, key, value):
        """Set a cache entry."""
        self.conn.execute(
            "INSERT OR REPLACE INTO cache (key, value, hits) VALUES (?, ?, 0)",
            (key, value),
        )
        self.conn.commit()

    def get(self, key):
        """Get a cache entry and increment hit counter."""
        row = self.conn.execute("SELECT value FROM cache WHERE key = ?", (key,)).fetchone()
        if row:
            self.conn.execute("UPDATE cache SET hits = hits + 1 WHERE key = ?", (key,))
            return row[0]
        return None

    def stats(self):
        """Get cache statistics."""
        rows = self.conn.execute("SELECT key, hits FROM cache ORDER BY hits DESC").fetchall()
        return {k: h for k, h in rows}

    def size(self):
        return self.conn.execute("SELECT COUNT(*) FROM cache").fetchone()[0]


if __name__ == "__main__":
    cache = InMemoryCache()
    cache.set("user:1", "Alice")
    cache.set("user:2", "Bob")
    for _ in range(5):
        cache.get("user:1")
    cache.get("user:2")
    print(f"user:1 = {cache.get('user:1')}")
    print(f"Cache size: {cache.size()}")
    print(f"Hit stats: {cache.stats()}")
