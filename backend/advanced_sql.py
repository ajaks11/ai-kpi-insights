import sqlite3

def get_user_activity():
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT users.name, COUNT(posts.id) AS post_count
        FROM users
        JOIN posts ON users.id = posts.user_id
        GROUP BY users.id
        ORDER BY post_count DESC
    """)

    results = cursor.fetchall()
    conn.close()

    return results
