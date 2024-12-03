from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_DB_SETTINGS['HOST'], settings.MONGO_DB_SETTINGS['PORT'])
db = client[settings.MONGO_DB_SETTINGS['NAME']]

class Consignment:
    collection = db.consignments

    @staticmethod
    def create(data):
        return Consignment.collection.insert_one(data)

    @staticmethod
    def find(query):
        return list(Consignment.collection.find(query))

    @staticmethod
    def update(query, data):
        return Consignment.collection.update_one(query, {'$set': data})

    @staticmethod
    def delete(query):
        return Consignment.collection.delete_one(query)
