--Query to count number of flights assigned to each pilot

.headers on
.mode column

SELECT 
p.name AS pilot_name,
p.pilotlicense AS pilot_license,
COUNT(f.flightID) OVER (PARTITION BY p.pilotID) AS total_flights, -- count used to aggregate and partition used to group rows by p.pilotID so each flight is counted 
f.flight_number,
f.departure_time,
f.arrival_time
FROM FLIGHT f
JOIN DESTINATION o ON f.originID = o.destinationID
JOIN DESTINATION d ON f.destinationID = d.destinationID
JOIN Pilot p ON f.pilotID = p.pilotID
ORDER BY total_flights DESC, f.departure_time ASC; -- sorts rows so that pilot with most flights appear at top and then sorting by departure time ascending
