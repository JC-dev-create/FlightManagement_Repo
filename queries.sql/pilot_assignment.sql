-- Query to assign a pilot to a flight

UPDATE FLIGHT
SET pilotID = 10
WHERE flight_number = 'AF200'; -- WHERE used to prevent updating every flight.  Flight AF200 only updated.  