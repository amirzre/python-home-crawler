import json
from abc import ABC, abstractmethod
from mongo import MongoDatabase


class StoraeAbstract(ABC):
    """Base class for inheritance in other classes"""

    @abstractmethod
    def store(self, data, *args):
        pass

    @abstractmethod
    def load(self, *args, **kwargs):
        pass


class MongoStorage(StoraeAbstract):
    """Store and load files from mongodb"""

    def __init__(self):
        self.mongo = MongoDatabase()

    def store(self, data, collection, *args):
        """Store data in mongodb"""
        collection = getattr(self.mongo.database, collection)
        if isinstance(data, list) and len(data) > 1:
            collection.insert_many(data)
        else:
            collection.insert_one(data)

    def load(self, collection_name, filter_data=None):
        """Loads links from mongodb"""
        collection = self.mongo.database[collection_name]
        if filter_data is not None:
            data = collection.find(filter_data)
        else:
            data = collection.find()
        return data

    def update_flag(self, data):
        """Update flag for links to prevent again crawl"""
        self.mongo.database.advertisements_links.find_one_and_update(
            {'_id': data['_id']},
            {'$set': {'flag': True}}
        )


class FileStorage(StoraeAbstract):
    """Store and load files from file"""

    def store(self, data, filename, *args):
        """Store data in files"""
        filename = f'{filename} - {data["post_id"]}'
        with open(f'fixtures/adv/{filename}.json', 'w') as f:
            f.write(json.dumps(data))
        print(f'fixtures/adv/{filename}.json')

    def load(self):
        """Loads links from file"""
        with open('fixtures/adv/advertisements_links.json', 'r') as f:
            links = json.loads(f.read())
        return links
