import sqlite3
import os


# Determine the mode to be used and get the database name
def setup():
    valid_mode = False
    database_name = ""
    mode = ""

    while not valid_mode:
        print("Enter 0 to create a new database or 1 to use an existing one")
        mode = input()
        if mode == "0" or mode == "1":
            valid_mode = True
            print("Please enter the name for the database")
            database_name = input()
        else:
            print("Invalid database name, please ensure you have no leading or trailing characters")
    return database_name, mode

# Parse the input file name and ensure it ends in .db and has no spaces
def parseDBName(database_name):
    return_string = database_name.strip()
    if return_string.find(".db") == -1:
        return_string += ".db"
    return return_string


# Create a new database file if requested
def createNewDatabase(mode, database_name):
    if os.path.exists(database_name):
        os.remove(database_name)
        
    new_db = open(database_name, "x")
    new_db.close()

    
def printHelp():
    print("\nHelp: here are the available commands (but exclude the quotation marks)")
    print("Create table: 'create'")
    print("Get columns of a table: 'cols")
    print("Add an item: 'item'")
    print("Add items from document: 'document'")
    print("Quit the program: 'exit'")


if __name__ == "__main__":
    # Display the startup menu with options
    print("Welcome to sqlite starter!")
    database_name, mode = setup()
    print()

    # Ensure they didn't add the '.db' to the input file
    database_name = parseDBName(database_name)

    # Create a database if needed
    if mode == 0:
        createNewDatabase(mode, database_name)
    
    # Connect to the database and get a cursor
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    # Setup Main Loop
    running = True

    while running:
        print()
        print("Please type in a command!")
        print("Note: use 'help' to see a list of options")
        selection = input().lower()

        if selection == 'help':
            printHelp()
        elif selection == 'exit':
            print("Take Care :)")
            running = False
        else:
            print("Error: Invalid command '{}' used.".format(selection))
        


    # Commit to the db and close the connection
    conn.commit()
    conn.close()








    

        