from flask import Flask, jsonify
from flask_cors import CORS

from database import init_db
from sql_kpis import get_kpis_from_sql
from ai_insights import generate_ai_insight
from advanced_sql import get_user_activity

app = Flask(__name__)
CORS(app)


@app.route("/health")
def health():
    return {"status": "API is running"}

@app.route("/kpis")
def kpis():
    kpis = get_kpis_from_sql()
    return jsonify(kpis)

@app.route("/ai-insight")
def ai_insight():
    kpis = get_kpis_from_sql()
    insight = generate_ai_insight(kpis)
    return {"insight": insight}

@app.route("/top-users")
def top_users():
    users = get_user_activity()
    return jsonify(users)

if __name__ == "__main__":
    print("Starting API server...")
    init_db()
    app.run(debug=True)
