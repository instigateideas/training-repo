import pymongo

database_name = "titanic_db"
collection_name = "passengers_collection"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[database_name]
mycol = mydb[collection_name]

myquery = {"PassengerId": 12}

x = mycol.delete_one(myquery)

print(x.deleted_count, " documents deleted.")