from pymongo import MongoClient

class MongoDBConnection:

    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://Arelis:Arelis2006@cluster0.qdn4zsf.mongodb.net/"
        )
        self.database = self.client["BookSalesDB"]

    def get_collection(self, name):
        return self.database[name]