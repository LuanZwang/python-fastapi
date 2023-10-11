from abc import ABCMeta
from datetime import datetime
from pymongo import MongoClient
from domain.model.database_model import IDatabaseModel

class BaseRepository():
    __metaclass__ = ABCMeta

    @classmethod
    def __init__(self, collectionName: str):
        self.connStr = 'mongodb://admin:admin@127.0.0.1:27017/'
        self.dbName = 'my-database'
        client = MongoClient(self.connStr)
        database = client[self.dbName]
        self.collection = database[collectionName]

    @classmethod
    def upsert(self, item: IDatabaseModel, ensureExists: bool =False) -> dict:
        
        if (ensureExists):
            createdAt = self.collection.find_one({ '_id': item._id }, { 'created_at': 1, '_id': 0})

            if createdAt is None:
                return { 'mesage': 'not found - id: %s' % (item._id) }
            
            item.created_at = createdAt['created_at']
            
        try:
            if not isinstance(item, IDatabaseModel): return { 'mesage': 'not a database model - id: %s' % (item._id) }

            itemDict = item.to_dict()
            self.collection.update_one({ '_id': item._id }, { '$set': itemDict }, upsert=True)
            
            return itemDict
        except Exception as e:
            return { 'message': 'erro inesperado - id: %s \n error: %s' % (item._id, e) }
