# Import the PyMongo library
import os.path
from pymongo import MongoClient
from dotenv.main import load_dotenv

# Create a new connection to the MongoDB server
load_dotenv()

token = os.getenv('token')

client = MongoClient(f"mongodb+srv://{token}@cluster0.dbu4l.mongodb.net/?retryWrites=true&w=majority")

def SignUp(id, name, passw):

    db = client.Accounts

    # Get a reference to the "my_collection" collection
    my_collection = db["Accounts"]

    # Query the "my_collection" collection for all documents
    results = my_collection.find({})

    my_collection.insert_one({"id": id, "name": name, "password": passw})

    # Print the results
    for result in results:
        print(result)

import datetime

now = datetime.datetime.now()
print(now)

def msg(channel, text, author, date = now):
    db = client.Msgs

    # Get a reference to the "my_collection" collection
    my_collection = db[channel]

    # Query the "my_collection" collection for all documents
    results = my_collection.find({})

    my_collection.insert_one({"author": author, "text": text, "date": date})

    # Print the results
    for result in results:
        print(result)