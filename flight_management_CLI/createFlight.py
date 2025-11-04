# adding a flight to the flightmanagement.db database

from database import connect # imports the connect function from database.py module

# defines function of createFlight and prompts user to input data in a certain format.  
def createFlight():
    conn = connect()
    c = conn.cursor()
    fn = input('Flight_number: ') # stops program and shows Flight_number.  The user input is captured as a string and stored in variable fn
    dt = input('departure_time (YYYY-MM-DD HH:MM): ')
    at = input('arrival_time (YYYY-MM-DD HH:MM): ')
    st = input('status: ')
    oi = input('originID select value between 1-10: ')
    di = input('destinationID select value between 1-10: ')
    pi = input('pilotID select value between 1-10: ')
    # INSERT into FLIGHT table using ? to pass values such as fn 
    c.execute('''               
              INSERT INTO FLIGHT  
              (flight_number, departure_time, arrival_time, status, originID, destinationID, pilotID)
              VALUES (?,?,?,?,?,?,?)
    ''',(fn,dt,at,st,oi,di,pi))
    conn.commit()
    conn.close() # closes the database connection
    # displays a confirmation to the user
    print('Flight added to Airline database. ')
if __name__ == "__main__":
    addFlight()
