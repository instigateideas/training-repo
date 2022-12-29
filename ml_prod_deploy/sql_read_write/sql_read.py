import pymysql
import pandas as pd

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='arun',
                             password='Test@123',
                             database='titanicdb',
                             cursorclass=pymysql.cursors.DictCursor)
print("connection to DB successfull")

qry = "SELECT * FROM passenger_table;"

with connection.cursor() as cursor:
    cursor.execute(qry)
    output = cursor.fetchall()

df =pd.DataFrame(output)
print(df.head())