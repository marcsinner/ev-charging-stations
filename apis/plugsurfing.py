import requests
import math
import pymongo
from repository.db import initDB
from repository.local_data_loader import loadLocalData


def load_one():
    collection = initDB("plugsurfing")
    r=requests.get("https://api.plugsurfing.com/mfund/stations?page=1&limit=1")
    data = r.json()[0]
    print(data)
    collection.insert_one(data)

def load_all(page_limit):
    collection = initDB("plugsurfing")
    r=requests.get("https://api.plugsurfing.com/mfund/stations?page=1&limit=1")
    pages=math.ceil(int(r.headers['X-Total-Count'])/100)
    page_amount = page_limit+1 if page_limit else pages+1
    for page in range(1,page_amount):
        print('load page number: ' + str(page))
        r=requests.get("https://api.plugsurfing.com/mfund/stations?page="+str(page)+"&limit=100")
        print('processing request for page: ' + str(page))
        print(len(r.json()))
        for i in range(len(r.json())):
            print(i)
            data = r.json()[i]
            collection.insert_one(data)

def load_from_local(filename):
    collection = initDB("plugsurfing_cologne")
    d = loadLocalData('data\\plugsurfing_cologne.json')
    for i in range(len(d)):
      print(i)
      data = d[i]
      collection.insert_one(data)    
            

if __name__ == '__main__':
    #load_all(page_limit=1)
    #load_one()
    load_from_local('data\\plugsurfing_cologne.json')