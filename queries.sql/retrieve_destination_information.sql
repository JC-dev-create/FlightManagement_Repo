-- Query to retrieve destination information for number of flights landing

.headers on
.mode column

SELECT d.city AS destination_city,
d.country AS destination_country,
COUNT(f.flightID) AS total_flights --Counts how many flights for each group
FROM FLIGHT f
JOIN DESTINATION d ON f.destinationID = d.destinationID
GROUP BY d.city, d.country --Groups the results by city and country
ORDER BY total_flights DESC; --Orders by descending order to show most flights to a destination first
