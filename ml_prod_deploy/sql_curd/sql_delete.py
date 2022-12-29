import pymysql
import pandas as pd

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='arun',
                             password='Test@123',
                             database='titanicdb',
                             cursorclass=pymysql.cursors.DictCursor)
print("connection to DB successfull")

delete_qry = "DELETE FROM passenger_table WHERE id=12"
find_deleted_qry = "SELECT * FROM passenger_table WHERE id=12"

# Update record
with connection.cursor() as cursor:
    cursor.execute(delete_qry)
    connection.commit()

print("Deleted the Record...")

# Get the updated record
with connection.cursor() as cursor:
    cursor.execute(find_deleted_qry)
    updated_row = cursor.fetchall()

print("Deleted Record")
for col in updated_row:
    print(col)