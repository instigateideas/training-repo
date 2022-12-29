import pymongo

database_name = "titanic_db"
collection_name = "passengers_collection"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[database_name]
mycol = mydb[collection_name]

myquery = { "_id": 12, "Name": "Bonnell, Miss. Elizabeth" }
newvalues = { "$set": { "Name": "Arunachalam Dharmaraj"}}

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)