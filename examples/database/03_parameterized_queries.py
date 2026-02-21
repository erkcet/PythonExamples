"""Parameterized queries to prevent SQL injection."""

import sqlite3


def setup_db():
    """Set up a test database."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    products = [("Widget", 9.99), ("Gadget", 24.99), ("Doohickey", 4.99)]
    conn.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
    conn.commit()
    return conn


def safe_search(conn, name):
    """Search using parameterized query (SAFE)."""
    return conn.execute("SELECT * FROM products WHERE name = ?", (name,)).fetchall()


def unsafe_search(conn, name):
    """Search using string formatting (UNSAFE - DO NOT USE)."""
    return conn.execute(f"SELECT * FROM products WHERE name = '{name}'").fetchall()


def search_by_price_range(conn, min_price, max_price):
    """Search with multiple parameters."""
    return conn.execute(
        "SELECT * FROM products WHERE price BETWEEN ? AND ?",
        (min_price, max_price),
    ).fetchall()


if __name__ == "__main__":
    conn = setup_db()
    print(f"Safe search: {safe_search(conn, 'Widget')}")
    print(f"Price range: {search_by_price_range(conn, 5.0, 25.0)}")
    malicious = "' OR '1'='1"
    print(f"\nMalicious input: {malicious!r}")
    print(f"Safe (returns nothing): {safe_search(conn, malicious)}")
    print("\nNote: Always use parameterized queries (?) to prevent injection!")
    conn.close()
