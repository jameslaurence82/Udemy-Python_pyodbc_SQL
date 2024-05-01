### Create EXE using GUI - Auto PY to EXE

# Import modules
import pyodbc
import csv

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # Create the table tblCustomersFromCSV
    createTableTSQL="""CREATE TABLE [dbo].[tblCustomersFromCSV2](
	[id] [int] NOT NULL,
	[code] [varchar](50) NULL,
	[firstName] [varchar](50) NULL,
	[lastName] [varchar](50) NULL,
    )"""
    
    cursor.execute(createTableTSQL)
    connection.commit()

    # SELECT Query Before INSERT
    cursor.execute("SELECT * FROM tblCustomersFromCSV2")

    print("[Before INSERT...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.id,row.code,row.firstName,row.lastName)

    print()

    #Read CSV File and Insert Rows to SQL Server Table
    print("[Reading CSV File and Insert Rows to SQL Server Table]")    
    with open('python/sample-csv-file-for-demo.csv') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvReader:
            prmID=row[0]
            prmCode=row[1]
            prmFirstName=row[2]
            prmLastName=row[3]

            print('Inserting record: ',', '.join(row))
            cursor.execute("INSERT INTO [tblCustomersFromCSV2] ([id],[code],[firstName],[lastName]) VALUES (?,?,?,?)",(prmID,prmCode,prmFirstName,prmLastName))

            connection.commit()
            
    print()

    # SELECT Query After INSERT
    cursor.execute("SELECT * FROM tblCustomersFromCSV2")

    print("[After INSERT...]")
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