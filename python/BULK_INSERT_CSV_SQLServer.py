# BULK_INSERT_CSV_SQLServer.py
#
# Created for the online course on Udemy: "Working with Python® on Windows® and SQL Server® Databases"
#
# Course URL: 
# https://www.udemy.com/course/python-windows-sql-server
#
# Author/Instructor: Artemakis Artemiou
#
# Disclaimer: This source code which is part of the online course on Udemy "Working with Python® on Windows® 
# and SQL Server® Databases", is intended to be used only for demo purposes. Do not 
# use it for Production systems as it is simplified for demo purposes.
#

# BULK INSERT CSV File Contents to SQL Server Table
# Note 1: The data file to be imported via the BULK INSERT command, must be located on the database server.
# Note 2: For this example, I'm using C:\Demos\sample-csv-file-for-demo.csv and I use semicolon for separating the

# Import modules
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQL2K19;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # Create the table tblCustomersFromCSV
    createTableTSQL="""CREATE TABLE [dbo].[tblCustomersFromCSV](
	[id] [int] NOT NULL,
	[code] [varchar](50) NULL,
	[firstName] [varchar](50) NULL,
	[lastName] [varchar](50) NULL,
    )"""
    
    cursor.execute(createTableTSQL)
    connection.commit()

    # SELECT Query Before BULK INSERT
    cursor.execute("SELECT * FROM tblCustomersFromCSV")

    print("[Before BULK INSERT...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.id,row.code,row.firstName,row.lastName)

    print()

    #Read CSV File and Insert Rows to SQL Server Table via the BULK INSERT COMMAND
    bulkInsertCommand="""BULK INSERT tblCustomersFromCSV
    FROM 'C:\Demos\sample-csv-file-for-demo.csv'  
    WITH   
      (  
         FIELDTERMINATOR =';',  
         ROWTERMINATOR ='\n'  
      );"""
    print("Running BULK INSERT command...")    
    cursor.execute(bulkInsertCommand)
    connection.commit()
    print("BULK INSERT command executed.")    

            
    print()

    # SELECT Query After INSERT
    cursor.execute("SELECT * FROM tblCustomersFromCSV")

    print("[After BULK INSERT...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.id,row.code,row.firstName,row.lastName)


    cursor.close()
    connection.close()

except pyodbc.Error as ex:
    print("Exception: ",ex)
    cursor.close()
    connection.close()
    print("Closing program...")
    print()
    exit()

print()