import os

def generate_ai_insight(kpis):
    prompt = (
        "You are a Senior Data Program Manager at a large tech company.\n\n"
        "Given the following KPIs from a user engagement platform:\n\n"
        f"{kpis}\n\n"
        "Your task:\n"
        "1. Identify key trends and anomalies\n"
        "2. Explain what the KPIs indicate about user behavior\n"
        "3. Suggest 2 actionable product or operations improvements\n"
        "4. Keep the explanation clear for non-technical stakeholders\n\n"
        "Write the response in a professional but human tone."
    )

    # TEMP fallback (safe if API fails)
    return (
        "User engagement appears concentrated among a small group of highly active users. "
        "This suggests opportunities to improve onboarding and re-engagement strategies for less active users. "
        "Operational focus should be placed on retention experiments and feature discovery improvements."
    )
