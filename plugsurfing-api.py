import requests
import math
import pymongo
from credentials import uri


def initDB():
    client = pymongo.MongoClient(uri)
    DB_NAME = "test-db"
    db = client[DB_NAME]
    collection = db.plugsurfing
    return collection

def load_one():
    collection = initDB()
    r=requests.get("https://api.plugsurfing.com/mfund/stations?page=1&limit=1")
    data = r.json()[0]
    print(data)
    collection.insert_one(data)

def load_all():
    collection = initDB()
    r=requests.get("https://api.plugsurfing.com/mfund/stations?page=1&limit=1")
    pages=math.ceil(int(r.headers['X-Total-Count'])/100)
    for page in range(1,pages+1):
        print('load page number: ' + str(page))
        r=requests.get("https://api.plugsurfing.com/mfund/stations?page="+str(page)+"&limit=100")
        print('processing request for page: ' + str(page))
        for i in range(len(r.json())):
            data = r.json()[i]
            collection.insert_one(data)

            

if __name__ == '__main__':
    load_all()