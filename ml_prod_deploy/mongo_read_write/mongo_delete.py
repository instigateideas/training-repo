import pymongo

database_name = "titanic_db"
collection_name = "passengers_collection"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[database_name]
mycol = mydb[collection_name]

myquery = { "_id": 12 }

mycol.delete_one(myquery)