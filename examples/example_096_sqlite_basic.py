import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (name TEXT, age INTEGER)")
cur.execute("INSERT INTO users VALUES (?, ?)", ("Ana", 30))
cur.execute("SELECT name, age FROM users")
print(cur.fetchall())
conn.close()
