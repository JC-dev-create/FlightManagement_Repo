-- Query to retrieve a pilots schedule of flights

.headers on
.mode column

SELECT
f.flightID,
f.flight_number,
f.departure_time,
f.arrival_time,
f.status,
o.airport AS origin_airport,
o.city AS origin_city,
o.country AS origin_country,
d.airport AS destination_airport,
d.city AS destination_city,
d.country AS destination_country,
p.name AS pilot_name,
p.pilotlicense AS pilot_license
FROM FLIGHT f 
JOIN DESTINATION o ON f.originID = o.destinationID
JOIN DESTINATION d ON f.destinationID = d.destinationID
JOIN PILOT p ON f.pilotID = p.pilotID
WHERE p.pilotID = 10 -- WHERE clause used to retrieve pilotID 10, in this case Julia Roberts
ORDER BY f.departure_time; -- ORDER BY clause used to sort the data by departure time