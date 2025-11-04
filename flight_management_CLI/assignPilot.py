# assigning a pilot to a flight

from database import connect

# define the function to assign a pilot
def assignPilot():
    flight_no = input("Enter flight_number to update the pilot for:") # prompt user for flight number input
    new_pilot = input("Enter new pilotID to assign the pilot: ") # prompts user to enter the new pilotID and stores in variable new_pilot

# query to update pilotID for the selected flight_number in FLIGHT table
    query = "UPDATE FLIGHT SET pilotID = ? WHERE flight_number = ?" # ? will be replaced with values at run time

    with connect() as conn:
        c = conn.cursor()
        c.execute(query, (new_pilot, flight_no))
        conn.commit()

# checks if more than 0 rows were updated meaning pilot was assigned successfully and prints message
# if no rows updated then error message printed
        if c.rowcount > 0:
            print(f"pilot {new_pilot} assigned to flight {flight_no}.") 
        else:
            print(f"No flight could be found with flight_number {flight_no}. ")

if __name__ == "__main__":
    assignPilot()