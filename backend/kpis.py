def calculate_kpis(users, posts):
    total_users = len(users)
    total_posts = len(posts)
    avg_posts_per_user = round(total_posts / total_users, 2)

    return {
        "total_users": total_users,
        "total_posts": total_posts,
        "avg_posts_per_user": avg_posts_per_user
    }
