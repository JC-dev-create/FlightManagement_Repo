-- Query to modify the destination of a flight

UPDATE FLIGHT
SET destinationID = 2 -- Updates the destination on the chosen flight number to London Heathrow
WHERE flight_number = 'VS1000';
