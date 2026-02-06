import logging
logging.basicConfig(level=logging.INFO)
from advanced_sql import get_user_activity
from data_sources import fetch_users, fetch_posts
from ai_insights import generate_ai_insight
from database import init_db, insert_users, insert_posts
from sql_kpis import get_kpis_from_sql


def main():
    print("APP STARTED")

    logging.info("Initializing database")
    init_db()

    print("Fetching data...")
    users = fetch_users()
    posts = fetch_posts()

    print("Saving data to database...")
    insert_users(users)
    insert_posts(posts)

    print("Calculating KPIs using SQL...")
    kpis = get_kpis_from_sql()

    print("\nKPI RESULTS")
    print("------------------")
    for key, value in kpis.items():
        print(f"{key}: {value}")

    print("\nAI INSIGHT")
    print("------------------")
    print(generate_ai_insight(kpis))

    print("\nTOP USERS BY ACTIVITY")
    print("------------------")
    top_users = get_user_activity()

    for name, count in top_users[:3]:
        print(f"{name}: {count} posts")


if __name__ == "__main__":
    main()
