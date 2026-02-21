"""Full CRUD operations with SQLite3."""

import sqlite3


class UserDB:
    """Simple CRUD wrapper for a users table."""

    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS users "
            "(id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
        )

    def create(self, name, email):
        """Create a new user."""
        cur = self.conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()
        return cur.lastrowid

    def read(self, user_id):
        """Read a user by ID."""
        return self.conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

    def update(self, user_id, **kwargs):
        """Update user fields."""
        sets = ", ".join(f"{k} = ?" for k in kwargs)
        self.conn.execute(f"UPDATE users SET {sets} WHERE id = ?", (*kwargs.values(), user_id))
        self.conn.commit()

    def delete(self, user_id):
        """Delete a user."""
        self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def list_all(self):
        return [dict(r) for r in self.conn.execute("SELECT * FROM users").fetchall()]


if __name__ == "__main__":
    db = UserDB()
    uid = db.create("Alice", "alice@test.com")
    print(f"Created user ID: {uid}")
    print(f"Read: {dict(db.read(uid))}")
    db.update(uid, name="Alice Smith", email="asmith@test.com")
    print(f"Updated: {dict(db.read(uid))}")
    db.create("Bob", "bob@test.com")
    print(f"All: {db.list_all()}")
    db.delete(uid)
    print(f"After delete: {db.list_all()}")
