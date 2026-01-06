from pymongo import MongoClient

class MongoDBConnection:
    _database = None

    def __init__(self):
        pass  

    @staticmethod
    def get_database():
        if MongoDBConnection._database is None:
            client = MongoClient(
                "mongodb+srv://Arelis:Arelis2006@cluster0.qdn4zsf.mongodb.net/"
            )
            MongoDBConnection._database = client["SalesDB"]

        return MongoDBConnection._database