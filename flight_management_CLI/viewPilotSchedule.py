# viewing a pilots schedule

from database import connect

# define a function for retrieving and then displaying a pilots schedule based on pilotID
def viewPilotSchedule():
    pilot_id = input("Enter pilotID to view their assigned schedule:  ") # prompt for pilotID

# SQL query to retrieve flight details based on user selected pilot_ID
    query = """
    SELECT
        f.flight_number,
        f.departure_time,
        f.arrival_time,
        f.status,
        o.city AS origin_city,
        o.airport AS origin_airport,
        d.city AS destination_city,
        d.airport as destination_airport
    FROM FLIGHT f
    JOIN destination o ON f.originID = o.destinationID
    JOIN DESTINATION d ON f.destinationID = d.destinationID
    WHERE f.pilotID = ?
    ORDER BY f.departure_time;
    """

# with used to close connection after query
    with connect() as conn:
        c = conn.cursor()
        c.execute(query, (pilot_id,))
        rows = c.fetchall()

# checks if any flights were found for the pilot, using each row as a tuple and displaying results to create a sentence
        if rows:
            print(f"\nSchedule for pilot {pilot_id}: ")
            for row in rows:
                print(
                    f"Flight {row[0]} | {row[4]} ({row[5]}) → {row[6]} ({row[7]}) "
                    f"| Dep: {row[1]} | Arr: {row[2]} | Status: {row[3]}"
                )
        else:
            print(f"No flights could be found for the pilot {pilot_id}.") # else statement to output if invalid pilotID input

if __name__ == "__main__":
    viewPilotSchedule()
