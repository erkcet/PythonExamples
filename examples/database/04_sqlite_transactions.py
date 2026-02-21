"""Transaction management with SQLite3."""

import sqlite3


def setup_db():
    """Create a bank accounts database."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL)")
    conn.executemany("INSERT INTO accounts (name, balance) VALUES (?, ?)",
                     [("Alice", 1000.0), ("Bob", 500.0)])
    conn.commit()
    return conn


def transfer(conn, from_id, to_id, amount):
    """Transfer money between accounts using a transaction."""
    try:
        with conn:
            bal = conn.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,)).fetchone()[0]
            if bal < amount:
                raise ValueError(f"Insufficient funds: {bal} < {amount}")
            conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))
            conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))
        return True
    except (ValueError, sqlite3.Error) as e:
        print(f"  Transfer failed: {e}")
        return False


def get_balances(conn):
    """Get all account balances."""
    return conn.execute("SELECT name, balance FROM accounts").fetchall()


if __name__ == "__main__":
    conn = setup_db()
    print(f"Before: {get_balances(conn)}")
    transfer(conn, 1, 2, 200.0)
    print(f"After $200 transfer: {get_balances(conn)}")
    transfer(conn, 1, 2, 5000.0)  # Should fail
    print(f"After failed transfer: {get_balances(conn)}")
    conn.close()
