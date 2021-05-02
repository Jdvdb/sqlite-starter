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
    print("Add an item to a table: 'item'")
    print("Add items from document to a table: 'document'")
    print("Quit the program: 'exit'")

# Function that will get info for the table and create it
def createTable():
    name, num_attributes, attributes = readTableInfo()

# Get all of the information from the user about the table
def readTableInfo():
    table_name = input("Please enter the table name: ")
    num_attributes = int(input("How many attributes will it have: "))
    attributes = []
    print("Please enter in the attributes as specified in the README")
    for i in range(num_attributes):
        temp_attribute = input("Attribute: ")
        attributes.append(temp_attribute)
    return table_name, num_attributes, attributes

# Breakdown the table input to be converted to SQLite
def parseTableReadInfo(attributes):
    att_names = []
    att_type = []
    att_null = []
    primary_atts = []
    foreign_atts = []
    for att in attributes:
        components = att.split()
        # get the name and type of each attribute first
        att_names.append(components[0])
        att_type.append(components[1])

        # determine if the value can be null
        if components[2] == 'nn':
            att_null.append(False)
        else:
            att_null.append(True)
        
        # add this to the primary key if applicable
        if components[2] == 'prim':
            primary_atts.append(len(att_names) - 1)

        # recognize this as a foreign key if applicable
        if components[2] == 'for':
            foreign_atts.append((len(att_names) - 1, components[3], components[4]))

    return att_names, att_type, att_null, primary_atts, foreign_atts
    
        



    

def getColumns():
    print("Getting Cols")

def addItem():
    print("Adding One Row")

def AddDocument():
    print("Adding all items from a document")


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
        elif selection == 'create':
            createTable()
        elif selection == 'cols':
            getColumns()
        elif selection == 'item':
            addItem()
        elif selection == 'document':
            AddDocument()
        elif selection == 'exit':
            print("Take Care :)")
            running = False
        else:
            print("Error: Invalid command '{}' used.".format(selection))
        


    # Commit to the db and close the connection
    conn.commit()
    conn.close()
