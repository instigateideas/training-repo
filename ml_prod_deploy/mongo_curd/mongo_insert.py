import pandas as pd
import pymongo

database_name = "titanic_db"
collection_name = "passengers_collection"

titanic_dataset = pd.read_csv("titanic.csv")

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


def insert_to_mongodb(mydict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[database_name]
    mycol = mydb[collection_name]

    x = mycol.insert_one(mydict)
    print(f"Inserted record: {x.inserted_id} to mongodb -> {database_name}")

for datum in titanic_dataset.to_dict(orient='records'):
    insert_to_mongodb(mydict=datum)