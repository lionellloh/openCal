import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None


    @staticmethod
    # We are telling python that this is not a method for the object instance, but for the class.
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    # Returns a cursor object
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    # Returns the json object
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)




