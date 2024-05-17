from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://siberia:rrUyQyWvzLOqDLkR@dave.qhyzhzr.mongodb.net/?retryWrites=true&w=majority&appName=Dave"
client = MongoClient(uri, server_api=ServerApi('1'))


db = client.doofenshmirtz_lab

#Collections
categories = db.categories


sample_types = db.sample_types

tests = db.tests

users = db.users


instructions = db.instructions