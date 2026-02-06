import sqlite3

def init_db():
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            title TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_users(users):
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    for user in users:
        cursor.execute(
            "INSERT OR IGNORE INTO users VALUES (?, ?, ?)",
            (user["id"], user["name"], user["email"])
        )

    conn.commit()
    conn.close()


def insert_posts(posts):
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    for post in posts:
        cursor.execute(
            "INSERT OR IGNORE INTO posts VALUES (?, ?, ?)",
            (post["id"], post["userId"], post["title"])
        )

    conn.commit()
    conn.close()
