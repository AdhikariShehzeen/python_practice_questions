from pymongo import MongoClient
import json

# Connect to MongoDB (default connection to localhost:27017)
client = MongoClient('mongodb://localhost:27017/')

print("ok")

db = client["test"]

# Select a collection

collection = db["JsonData"]

print("ok")
path = 'jsondata.json'
with open(path,'r') as json_file:
  data = json.load(json_file)


collection.insert_many(data)
