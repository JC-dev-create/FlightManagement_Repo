# Create, Remove, Update, Delete operations testing for Flights

# modules imported including the functional modules created

from pathlib import Path
import sqlite3
from createFlight import createFlight
from viewFlights import viewFlights
from updateFlightStatus import updateFlightStatus
from deleteFlight import deleteFlight
from assignPilot import assignPilot
from viewPilotSchedule import viewPilotSchedule
from viewUpdateDestination import viewUpdateDestination

#ensures script only runs when executed and uses a while loop to repeatedly show menu until exit chosen
if __name__ == "__main__": 
    while True:
        print("\n     Flight Management     ")
        print("1 - Create Flight")
        print("2 - viewFlights")
        print("3 - Update Flight Status")
        print("4 - Delete Flight")
        print("5 - Assign Pilot")
        print("6 - viewPilotSchedule")
        print("7 - viewUpdateDestination")
        print("8 - Exit")

        choice = input("Choose an option from 1 to 8: ")

        if choice == "1":
            createFlight()
        elif choice == "2":
            viewFlights()
        elif choice == "3":
            updateFlightStatus()
        elif choice == "4":
            deleteFlight()
        elif choice == "5":
            assignPilot()
        elif choice == "6":
            viewPilotSchedule()
        elif choice == "7":
            viewUpdateDestination()
        elif choice == "8":
            break
        else: # captures invalid inputs, prints an error and displays the menu choice
            print("Invalid input, select a number from 1 to 8.") 
