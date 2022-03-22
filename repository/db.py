import pymongo
from credentials import uri

def initDB(COLLECTION_NAME):
    DB_NAME = "test-db"
    client = pymongo.MongoClient(uri)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

def main():
    client = pymongo.MongoClient(uri)

    DB_NAME = "test-db"

    db = client[DB_NAME]
    collection = db.stations

    #document_id =insert_data(collection)
    # DELETE
    #collection.delete_one({"_id":'6230b3da85385a93c16f372d' })
    # INSERT
    #document_id = collection.insert_one({'sample_field': 'hello world'}).inserted_id
    # QUERY
    #id = collection.find_one({"_id": '6230b3da85385a93c16f372d'})


if __name__ == '__main__':
    main()