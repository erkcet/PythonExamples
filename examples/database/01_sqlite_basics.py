"""SQLite3 basics: create tables, insert, and query."""

import sqlite3


def create_database(db_path=":memory:"):
    """Create a database with a users table."""
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
    """)
    conn.commit()
    return conn


def insert_users(conn, users):
    """Insert multiple users into the database."""
    conn.executemany(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users
    )
    conn.commit()


def query_all(conn):
    """Query all users."""
    return conn.execute("SELECT * FROM users").fetchall()


if __name__ == "__main__":
    conn = create_database()
    users = [("Alice", "alice@example.com", 30), ("Bob", "bob@example.com", 25),
             ("Charlie", "charlie@example.com", 35)]
    insert_users(conn, users)
    print("All users:")
    for row in query_all(conn):
        print(f"  {row}")
    print(f"\nCount: {conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]}")
    conn.close()
