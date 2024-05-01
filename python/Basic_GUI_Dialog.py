# Create a Basic GUI Dialog to Connect  too SQL Server

# Import modules
from tkinter import *
import pyodbc

# Variable initialization
SQLServerVer = "Not Available"

# Set the main GUI window properties
window = Tk()
window.geometry('600x400')
window.title('Sample Python GUI App')

# Define label as part of tkinterface
lblHelloWorld = Label(window, text =str(SQLServerVer),fg='red') #fg is the foreground color

# Event handling code for the "Retrieve SQL Server Version" button
def SQLServerVersion (): 

    # Exception Handling
    try:
        # Trusted Connection to SQL Server Default Instance without Exception Handling
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=sampleDB;Trusted_Connection=yes;')

        # initialize the cursor with connection name
        cursor = connection.cursor()
        print()
        print('Successfully Connected to Database')
        print()

        # Retrieve SQL Server version info @@ is global variable
        cursor.execute("SELECT @@VERSION as version")

        while 1:
            row = cursor.fetchone()
            if not row:
                break
            SQLServerVer=row.version

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print()
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()

    # Set the label value
    lblHelloWorld.config(text = str(SQLServerVer)) # contents of updated variable
    lblHelloWorld.pack() # .pack() shows the label on main window

# Create "Retrieve SQL Server Version" button 
# command is the function SQLServerVersion when button is clicked
# text is the text in the button
btnSQLVersion = Button(window,command=SQLServerVersion, text = 'Retrieve SQL Server Version')
# indicates where the button is located
btnSQLVersion.pack(side = TOP, pady = 50)

# Display the GUI window
window.mainloop()
