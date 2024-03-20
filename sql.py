import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

## Create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert into STUDENT values('Krish', 'DATA SCIENCE', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('Ajay', 'DATA SCIENCE', 'B', 86)''')
cursor.execute('''Insert into STUDENT values('Bilal', 'SOFTWARE ENGINEER', 'C', 78)''')
cursor.execute('''Insert into STUDENT values('Sheraz', 'DATA SCIENCE', 'A', 92)''')
cursor.execute('''Insert into STUDENT values('Vishal', 'SOFTWARE ENGINEER', 'A', 90)''')

## Display all records
print("The inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()