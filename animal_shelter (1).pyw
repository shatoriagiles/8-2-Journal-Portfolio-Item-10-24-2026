from pymongo import MongoClient


class AnimalShelter:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.client = MongoClient(
            f"mongodb://{self.username}:{self.password}@localhost:27017/?authSource=admin"
        )

        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        try:
            if data is not None:
                self.collection.insert_one(data)
                return True
            else:
                return False

        except Exception as error:
            print(error)
            return False

    def read(self, query):
        try:
            results = self.collection.find(query)
            return list(results)

        except Exception as error:
            print(error)
            return []