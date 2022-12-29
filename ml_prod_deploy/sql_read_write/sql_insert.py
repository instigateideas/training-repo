import pandas as pd
import pymysql

# Read data
titanic_dataset = pd.read_csv("./titanic.csv")

# Make a copy for slicing
titanic_dataset = titanic_dataset.copy()

# Apply 2 decimal precision on fare
titanic_dataset["Fare"] = titanic_dataset["Fare"].apply(lambda x: "%.2f" % x)

# Impute median for Age which are missing
median_age = titanic_dataset["Age"].median()
# Fill the age column with the median age
titanic_dataset.loc[((titanic_dataset["Age"].isna()) | (titanic_dataset["Age"] == 0)), "Age"] = median_age

# Change the datatype of fare to float
titanic_dataset["Age"] = titanic_dataset["Age"].astype(int)
titanic_dataset["Fare"] = titanic_dataset["Fare"].astype(float)

# fill nan with empty string
titanic_dataset.fillna("X", inplace=True)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='arun',
                             password='Test@123',
                             database='titanicdb',
                             cursorclass=pymysql.cursors.DictCursor)
print("connection to DB successfull")

column_names = titanic_dataset.columns
column_names = [x.lower() for x in column_names]
column_names[0] = "id"
column_names = tuple(column_names)

def get_values_tuple(x):
    return "%s, "*len(x)


for i in titanic_dataset.itertuples(index=False, name=None):
    value_tuple = get_values_tuple(i)
    qry = "INSERT INTO `passenger_table` (id, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    with connection.cursor() as cursor:
        cursor.execute(qry, i)

    connection.commit()