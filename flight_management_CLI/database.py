# database accessor

import sqlite3 # import sqlite library to enable connecting and interacting with the flightmanagement.db created
from pathlib import Path

DB = Path(__file__).parent / "flightmanagement.db" # defines constant-like variable DB to reference the flight management database

def connect(): # connects to the database
    conn = sqlite3.connect(DB) # opens the database
    conn.execute('PRAGMA foreign_keys = ON;') # enforces foreign keys to ensure that only valid destinationID, pilotID or originID can be used 
    return conn