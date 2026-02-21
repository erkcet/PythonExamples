"""Aggregate queries with SQLite3: SUM, AVG, COUNT, GROUP BY."""

import sqlite3


def setup_db():
    """Create a sales database with sample data."""
    conn = sqlite3.connect(":memory:")
    conn.execute("""
        CREATE TABLE sales (
            id INTEGER PRIMARY KEY, product TEXT,
            category TEXT, amount REAL, quantity INTEGER
        )
    """)
    data = [("Widget", "A", 10.0, 5), ("Gadget", "B", 25.0, 3),
            ("Widget", "A", 10.0, 8), ("Doohickey", "A", 5.0, 12),
            ("Gadget", "B", 25.0, 1), ("Thingamajig", "C", 50.0, 2)]
    conn.executemany("INSERT INTO sales (product, category, amount, quantity) VALUES (?,?,?,?)", data)
    conn.commit()
    return conn


def sales_summary(conn):
    """Get overall sales summary."""
    return conn.execute("""
        SELECT COUNT(*) as count, SUM(amount * quantity) as total,
               AVG(amount) as avg_price, MAX(amount) as max_price
        FROM sales
    """).fetchone()


def sales_by_category(conn):
    """Group sales by category."""
    return conn.execute("""
        SELECT category, COUNT(*) as items, SUM(amount * quantity) as revenue
        FROM sales GROUP BY category ORDER BY revenue DESC
    """).fetchall()


if __name__ == "__main__":
    conn = setup_db()
    count, total, avg, mx = sales_summary(conn)
    print(f"Summary: {count} sales, total=${total:.2f}, avg=${avg:.2f}, max=${mx:.2f}")
    print("\nBy category:")
    for cat, items, rev in sales_by_category(conn):
        print(f"  {cat}: {items} items, ${rev:.2f} revenue")
    conn.close()
