import pandas as pd

df = pd.read_csv(
    "data/yellow_tripdata_sample.csv",
    parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"]
)

df.to_csv("data/cleaned_trips.csv", index=False)

print("Data loaded and cleaned successfully")
