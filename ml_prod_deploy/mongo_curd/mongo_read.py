import pymongo

database_name = "titanic_db"
collection_name = "passengers_collection"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[database_name]
mycol = mydb[collection_name]

# Get all the records in the collection
for x in mycol.find({}):
  print(x)

# Find the collection with id 12
for x in mycol.find({"PassengerId": 12}):
  print(x)