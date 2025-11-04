-- Create tables for the 3 main entities

PRAGMA foreign_keys = on;

DROP TABLE IF EXISTS DESTINATION;
DROP TABLE IF EXISTS PILOT;
DROP TABLE IF EXISTS FLIGHT;

Create TABLE DESTINATION (
    destinationID INTEGER PRIMARY KEY,
    airport TEXT UNIQUE,
    city TEXT,
    country TEXT
    );

CREATE TABLE PILOT (
    pilotID INTEGER PRIMARY KEY,
    name TEXT,
    pilotlicense TEXT UNIQUE
    );

CREATE TABLE FLIGHT (
    flightID INTEGER PRIMARY KEY,
    flight_number TEXT UNIQUE,
    departure_time TEXT,
    arrival_time TEXT,
    status TEXT,
    originID INTEGER REFERENCES DESTINATION(destinationID),
    destinationID INTEGER REFERENCES DESTINATION(destinationID),
    pilotID INTEGER REFERENCES PILOT(pilotID)
);
