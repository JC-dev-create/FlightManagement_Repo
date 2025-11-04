# view a destination and then update the details as required

from database import connect

# defines a function that vies and updates destination details 
def viewUpdateDestination():
    destination_id = input("Enter destinationID to update: ") # prompt user for destination_id

    # view the current destination details
    with connect() as conn:
        c = conn.cursor()
        c.execute(
            "SELECT destinationID, airport, city, country FROM DESTINATION WHERE destinationID = ?",
            (destination_id,)  
        )
        row = c.fetchone() # fetch the destination details 

        if not row:  # if statement used in the event no destination_id is matched
            print(f"No destination has been found with ID {destination_id}.")
            return
    
        print(f"\nCurrent details for destination {row[0]}:")
        print(f"Airport: {row[1]}")
        print(f"city: {row[2]}")
        print(f"Country: {row[3]}")

    # confirm with the user that they want to update the destination details
    confirm = input("\nDo you want to update this destination? (y/n):  ").lower()
    if confirm != "y":
        print("update cancelled.")
        return

    # check with the user which field they want to update
    print("\nwhich field do you want to update?")
    print("1 - Airport")
    print("2 - City")
    print("3 - Country") 
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        field, new_value = "airport", input("Enter new airport 3 letter code: ")
    elif choice =="2":
        field, new_value = "city", input("Enter new city: ")
    elif choice == "3":
        field, new_value = "country", input("Enter new country: ")
    else:
        print("Choice is Invalid.")
        return

    # parameterised SQL query to update the destination details
    query = f"UPDATE DESTINATION SET {field} = ? WHERE destinationID = ?"

    with connect() as conn:
        c = conn.cursor()
        c.execute(query, (new_value, destination_id))
        conn.commit()

# if and else used to check if any rows affected and prints output message
        if c.rowcount > 0:
            print(f"{field.capitalize()} updated successfully for destination {destination_id}. ")
        else:
            print(f"Update failed - no destination found with ID {destination_id}.")

if __name__ == "__main__":
    viewUpdateDestination()
