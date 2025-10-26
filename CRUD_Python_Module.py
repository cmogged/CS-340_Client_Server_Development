# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 
from pprint import pprint

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 
    
    def __init__(self, USER, PASS, HOST, PORT, DB, COL): 
        
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        """
        USER = 'aacuser' 
        PASS = 'password123' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        """
        # 
        # Initialize Connection 
        # 
        print("INITIALIZING CONNECTION")
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
        
        #pprint(self.client.admin.command('ping'))
        #pprint(self.client.server_info())
        #pprint(self.client.list_database_names())
        pprint(self.client.admin.command('usersInfo'))
        print("")
        
    # Create a method to return the next available record number for use in the create method
    def create(self, data):
        if data is not None: 
            try:
                result = self.database.animals.insert_one(data)  # data should be dictionary
                return True # result.inserted_id exists
            except Exception as e:
                print("Insertion failed:%s\n", e)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty") 
            #print("Nothing to save, because data parameter is empty\n")
            #return False # return false if empty
            
    
    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None: 
            result = self.database.animals.find(data) 
            return result    
        else:
            print("Nothing to read, because data parameter is empty\n")
            return []
    
    # update method
    def update(self, search_data, replace_data):
        try:
            result = self.database.animals.update_one(search_data, replace_data) 
            return result.modified_count
        except Exception as e:
            print("Update failed:%s\n", e)
            return 0
    
    # delete method
    def delete(self, data):
        try:
            result = self.database.animals.delete_one(data)
            return result.deleted_count
        except Exception as e:
            print("Deletion failed:%s\n", e)
            return 0