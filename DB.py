import os.path
from pymongo import MongoClient
from dotenv.main import load_dotenv

load_dotenv()

token = os.getenv('token')

client = MongoClient(f"mongodb+srv://{token}@cluster0.dbu4l.mongodb.net/?retryWrites=true&w=majority")

def SignUp(id, name, passw):
    db = client.Accounts
    my_collection = db["Accounts"]
    results = my_collection.find({})
    my_collection.insert_one({"id": id, "name": name, "password": passw})
    for result in results:
        print(result)

import datetime

now = datetime.datetime.now()
print(now)

def msg(channel, text, author, date = now):
    db = client.Msgs
    my_collection = db[channel]
    results = my_collection.find({})
    my_collection.insert_one({"author": author, "text": text, "date": date})
    for result in results:
        print(result)

def createServer(id, name):
    db = client.Servers
    my_collection = db[id]
    results = my_collection.find({})
    my_collection.insert_one({"id": id, "name": name})
    for result in results:
        print(result)

def createChan(id, name):
    db = client.Channels
    my_collection = db[id]
    results = my_collection.find({})
    my_collection.insert_one({"id": id, "name": name})
    for result in results:
        print(result)
