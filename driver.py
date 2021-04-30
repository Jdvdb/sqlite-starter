import sqlite3


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
    



if __name__ == "__main__":
    # Display the startup menu with options
    print("Welcome to sqlite starter!")
    database_name, mode = setup()
    print()






    

        