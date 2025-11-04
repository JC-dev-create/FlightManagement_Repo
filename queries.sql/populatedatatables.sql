-- Populating the data tables using the INSERT function

DELETE FROM DESTINATION;
DELETE FROM PILOT;
DELETE FROM FLIGHT;

INSERT INTO DESTINATION (destinationID, airport, city, country) VALUES
 (1,'GLA','Glasgow','UK'),
 (2,'LHR','London','UK'),
 (3,'CDG','Paris','France'),
 (4,'JFK','New York','USA'),
 (5,'DXB','Dubai','UAE'),
 (6,'HND','Tokyo','Japan'),
 (7,'SYD','Sydney','Australia'),
 (8,'YYZ','Toronto','Canada'),
 (9,'GRU','São Paulo','Brazil'),
 (10,'FRA','Frankfurt','Germany');

INSERT INTO PILOT (pilotID, name, pilotlicense) VALUES
 (1, 'Alice Smith', 'LIC1001'),
 (2, 'Bob Johnson', 'LIC1002'),
 (3, 'Charlie Brown', 'LIC1003'),
 (4, 'Diana Prince', 'LIC1004'),
 (5, 'Ethan Hunt', 'LIC1005'),
 (6, 'Fiona Gallagher', 'LIC1006'),
 (7, 'George Miller', 'LIC1007'),
 (8, 'Hannah Lee', 'LIC1008'),
 (9, 'Ian Wright', 'LIC1009'),
 (10, 'Julia Roberts', 'LIC1010');

 INSERT INTO FLIGHT (flightID, flight_number, departure_time, arrival_time, status, originID, destinationID, pilotID) VALUES  

     (1, 'BA100', '2025-10-03 08:00', '2025-10-03 10:00', 'On Time', 1, 2, 1),   -- Glasgow → London, Alice
 (2, 'AF200', '2025-10-03 09:30', '2025-10-03 12:00', 'On Time', 2, 3, 2),   -- London → Paris, Bob
 (3, 'DL300', '2025-10-03 11:00', '2025-10-03 14:00', 'Delayed', 3, 4, 3),   -- Paris → New York, Charlie
 (4, 'EK400', '2025-10-03 15:00', '2025-10-03 23:00', 'On Time', 5, 6, 4),   -- Dubai → Tokyo, Diana
 (5, 'QF500', '2025-10-04 07:00', '2025-10-04 19:00', 'Cancelled', 7, 8, 5), -- Sydney → Toronto, Ethan
 (6, 'AC600', '2025-10-04 10:00', '2025-10-04 18:00', 'On Time', 8, 9, 6),   -- Toronto → São Paulo, Fiona
 (7, 'LH700', '2025-10-04 12:00', '2025-10-04 16:00', 'On Time', 9, 10, 7),  -- São Paulo → Frankfurt, George
 (8, 'JL800', '2025-10-04 14:00', '2025-10-04 22:00', 'Delayed', 6, 7, 8),   -- Tokyo → Sydney, Hannah
 (9, 'UA900', '2025-10-05 06:00', '2025-10-05 12:00', 'On Time', 4, 5, 9),   -- New York → Dubai, Ian
 (10, 'VS1000', '2025-10-05 09:00', '2025-10-05 11:00', 'On Time', 2, 1, 10);-- London → Glasgow, Julia
 
