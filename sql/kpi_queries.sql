SELECT
  DATE(tpep_pickup_datetime) AS trip_date,
  COUNT(*) AS total_trips,
  AVG(trip_distance) AS avg_distance,
  AVG(fare_amount) AS avg_revenue
FROM trips
GROUP BY trip_date
ORDER BY trip_date;
