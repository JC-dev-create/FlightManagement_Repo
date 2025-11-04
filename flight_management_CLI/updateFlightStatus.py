#updateFlightStatus

from database import connect

def updateFlightStatus():
    flight_no = input("Enter the flight number you wish to update:")

    # View the current flight details
    with connect() as conn:
        c=conn.cursor()
        c.execute(
            """SELECT flight_number, departure_time, arrival_time, status 
               FROM FLIGHT WHERE flight_number = ? """,
            (flight_no,)
        )
        row = c.fetchone()
        
        # If no result found, informs the user and returns to the menu options. 
        if not row:
            print(f"No flight found with number {flight_no}. ")
            return
        
        print(f"\ncurrent details for flight {row[0]}:")
        print(f"Departure: {row[1]}")
        print(f"Arrival: {row[2]}")
        print(f"Status: {row[3]}")

    # Confirm with the user whether they wish to update the flights status
    confirm = input("\nDo you wish to update the flights status? (y/n): ").lower()
    if confirm != "y":
        print("Update cancelled.")
        return
    
    # Enter the new status
    new_status = input("Enter new status (On Time, Delayed, Cancelled, Rescheduled): ")
    
    # Update the flight status basis user input
    query = "UPDATE FLIGHT SET status = ? WHERE flight_number = ?"

    with connect() as conn:
        c=conn.cursor()
        c.execute(query, (new_status, flight_no))
        conn.commit()

    if c.rowcount > 0:
        print(f"Flight {flight_no} status has been updated to '{new_status}'.")
    else:
        print(f"Update failed - no flight could be found with  number {flight_no}.")

if __name__ == "__main__":
    updateFlightStatus()
    

    