import sqlite3

def get_kpis_from_sql():
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM posts")
    total_posts = cursor.fetchone()[0]

    avg_posts_per_user = round(total_posts / total_users, 2)

    conn.close()

    return {
        "total_users": total_users,
        "total_posts": total_posts,
        "avg_posts_per_user": avg_posts_per_user
    }
