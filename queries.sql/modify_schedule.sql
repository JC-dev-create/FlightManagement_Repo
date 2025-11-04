-- Query to modify the schedule of a flight

UPDATE FLIGHT
SET departure_time = '2025-10-04 09:00',
arrival_time = '2025-10-04 11:00',
status = 'Rescheduled'
WHERE flight_number = 'BA100';