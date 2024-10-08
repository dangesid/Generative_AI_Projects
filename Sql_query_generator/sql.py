import sqlite3

## Connect to sqlite

connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrive
cursor = connection.cursor()

## Create a table 
table_info = """

Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)

"""

cursor.execute(table_info)

## Insert SOME RECORDS

cursor.execute('''Insert into STUDENT values('Antman','Antropology','A',90)''')
cursor.execute('''Insert into STUDENT values('Batman','Neurology','B',100)''')
cursor.execute('''Insert into STUDENT values('Catman','Devops','A',80)''')
cursor.execute('''Insert into STUDENT values('Developer','Python','A',95)''')
cursor.execute('''Insert into STUDENT values('Engineer','Devops','A',98)''')
cursor.execute('''Insert into STUDENT values('FlaskMan','Flask','A',87)''')

## Display all records 

print("The inserted records are :")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection 

connection.commit()
connection.close()
