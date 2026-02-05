import pandas as pd

df = pd.read_csv(
    "data/cleaned_trips.csv",
    parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"]
)

df["trip_duration"] = (
    df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
).dt.total_seconds() / 60

df["date"] = df["tpep_pickup_datetime"].dt.date

kpis = df.groupby("date").agg(
    total_trips=("VendorID", "count"),
    avg_trip_duration=("trip_duration", "mean"),
    avg_distance=("trip_distance", "mean"),
    avg_revenue=("fare_amount", "mean")
).reset_index()

kpis.to_csv("outputs/daily_kpis.csv", index=False)

print("KPIs calculated successfully")
