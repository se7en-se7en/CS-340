from pymongo import MongoClient # this import allows to connect to our mongodb database
from bson.objectid import ObjectId #query using an ObjectID


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

#initialize the class for CRUD manipulation in the Mongo database
    def __init__(
        self, username=None, password=None
    ):
        if password and username:
            self.client = MongoClient(
                
                'mongodb://%s:%s@localhost:44107/aac' % (username, password)
            )
        else:
            self.client = MongoClient(
                "mongodb://127.0.0.1:44107"
            )
        self.database = self.client["aac"]

    # Create method to implement the C in CRUD.
    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except Exception as e:
            print(str(e))
            return False

            

    # Read method to implement the R in CRUD.
    def read(self, filter_data=None):  
        if filter_data: 
            animal_query = self.database.animals.find(
                filter_data, {"_id": False}
            )  
        else:  
            animal_query = self.database.animals.find({}, {"_id": False})
        return animal_query
    
     # Update method to implement the U in CRUD.
    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {'$set': update_data})
            return json.loads(result.raw_result)
        except Exception as e:
            return {"error": str(e)}

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return json.loads(result.raw_result)
        except Exception as e:
            return {"error": str(e)}
        
