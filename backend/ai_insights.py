def generate_ai_insight(kpis):
    return (
        f"The platform has {kpis['total_users']} users generating "
        f"{kpis['total_posts']} activities. "
        f"Each user contributes an average of "
        f"{kpis['avg_posts_per_user']} actions, "
        "indicating healthy engagement."
    )
