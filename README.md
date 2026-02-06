**# AI KPI Insights Dashboard**



An end-to-end analytics and AI project that demonstrates how raw data can be transformed into KPIs, business insights, and visual dashboards using Python, SQL, APIs, and LLMs.



This project simulates how a Data / Program Manager at a tech company (e.g., Uber) would design and deliver a data-driven analytics solution.



---



**## Project Overview**



The system performs the following steps:



1\. Fetches real user and activity data from a free public API

2\. Stores the data in a local SQLite database

3\. Calculates key performance indicators (KPIs) using SQL

4\. Uses an LLM (via API) to generate business insights from KPIs

5\. Exposes analytics via a Flask REST API

6\. Displays KPIs, AI insights, and charts in a frontend dashboard



---



**## Architecture**



ai-kpi-insights

│

├── backend

│ ├── app.py # Orchestrates data pipeline

│ ├── api.py # Flask API

│ ├── database.py # SQLite setup and inserts

│ ├── sql\_kpis.py # KPI calculations using SQL

│ ├── advanced\_sql.py # Advanced SQL analysis

│ ├── ai\_insights.py # LLM-based insight generation

│ └── analytics.db # Local database (gitignored)

│

├── frontend

│ └── index.html # Dashboard UI with charts

│

├── .gitignore

├── .env.example

└── README.md





---



**## Key KPIs Tracked**



\- Total number of users

\- Total number of posts / activities

\- Average posts per user

\- Most active users by engagement



These KPIs simulate real-world product and operations metrics.



---



**## AI Insights**



The project uses a structured prompt to convert KPIs into:

\- Human-readable insights

\- Behavioral observations

\- Actionable product or operational recommendations



This mirrors how analytics insights are presented to stakeholders.



---



**## Tech Stack**



\- Python 3

\- SQLite

\- SQL (joins, aggregation, grouping)

\- Flask (REST API)

\- JavaScript (native, no libraries)

\- HTML/CSS

\- LLM API integration (via environment variables)



---



**## How to Run the Project (Windows)**



\### 1. Clone the repository

```bash

git clone https://github.com/your-username/ai-kpi-insights.git

cd ai-kpi-insights



