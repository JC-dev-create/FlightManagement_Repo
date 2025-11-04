# reviewing all flights in a table format

from database import connect
from tabulate import tabulate # import to load tabulate library to format data into a structured table in the terminal

# declares viewFlights function to connect to flightmanagement.db and run a SELECT query to retrieve flight details from FLIGHT,
# origin and destination airport details from DESTINATION   and pilot_name from PILOT table.
# joins used to link rows in seperate tables and aliases for neatness of code

def viewFlights():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        SELECT
            f.flight_number,
            f.departure_time,
            f.arrival_time,
            f.status, 
            o.airport AS origin_airport,
            d.airport AS destination_airport,
            p.name AS pilot_name
        FROM FLIGHT f
        JOIN DESTINATION o ON f.originID = o.destinationID
        JOIN DESTINATION d ON f.destinationID = d.destinationID
        JOIN PILOT p on f.pilotID = p.pilotID
    ''')
    rows = c.fetchall()
    conn.close()

    headers = ["flight number", "departure time","arrival time", "status", "origin", "destination", "pilot"]
    print(tabulate(rows, headers=headers, tablefmt="grid")) # prints rows with headers to terminal in a table format for user friendly display

              