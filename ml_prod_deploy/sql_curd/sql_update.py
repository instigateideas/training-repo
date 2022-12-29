import pymysql
import pandas as pd

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='arun',
                             password='Test@123',
                             database='titanicdb',
                             cursorclass=pymysql.cursors.DictCursor)
print("connection to DB successfull")

update_qry = "UPDATE passenger_table set name = 'Arunachalam Dharmaraj' where id=12"
find_qry = "SELECT * FROM passenger_table where id=12;"

# Update record
with connection.cursor() as cursor:
    cursor.execute(update_qry)

# Get the updated record
with connection.cursor() as cursor:
    cursor.execute(find_qry)
    updated_row = cursor.fetchall()

print("Updated Record")
for col in updated_row:
    print(col)