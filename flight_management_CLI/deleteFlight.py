# deleting a flight in the flightmanagement.db database

from database import connect

def deleteFlight():
    fn = input("enter flight_number to delete it: ")
    with connect() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM FLIGHT WHERE flight_number = ?", (fn,))
        conn.commit()
        print(f"Attempted to delete flight {fn}. ")

if __name__ == "__main__":
    deleteFlight()

    
