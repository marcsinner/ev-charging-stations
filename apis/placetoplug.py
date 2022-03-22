import requests
import math
import pymongo
from repository.db import initDB
from repository.local_data_loader import loadLocalData


url = "https://api.placetoplug.com/go/graphql"

query = """query Query ($query: FindChargingZone!) {
  findChargingZones(query: $query) {
    chargingZones {
      id
      name
      description
      status
      coordinates
      vehicleTypes
      isPtP
      isPublic
      reviews {
        reviews {
          id
          comment
        }
        totalCount
      }
      stations {
        id
        name
        status
        services {
          id
          name
          status
          plugs {
            id
            status
            name
            current
            power
            plugFormat
          }
        }
      }
    }
    totalCount
		hasNextPage
  }
}
"""

def load_one():
    collection = initDB("placetoplug")
    #TODO adjust queery variables
    variables = {"query": {"limit":2}}
    r=requests.post(url, json={"query": query, "variables":variables, "operationName": 'Query' } )
    data = r.json()["data"]["findChargingZones"]["chargingZones"][0]
    print(data)
    collection.insert_one(data)

def load_all():
    collection = initDB("placetoplug")
    variables = {"query": {"limit":50}}
    r=requests.post(url, json={"query": query, "variables":variables, "operationName": 'Query' } )
    for i in range(len(r.json()["data"]["findChargingZones"]["chargingZones"])):
      print(i)
      data = r.json()["data"]["findChargingZones"]["chargingZones"][i]
      collection.insert_one(data)

def load_from_local(filename):
    collection = initDB("placetoplug_cologne")
    d = loadLocalData('data\\placetoplug_cologne.json')
    for i in range(len(d["data"]["findChargingZones"]["chargingZones"])):
      print(i)
      data = d["data"]["findChargingZones"]["chargingZones"][i]
      collection.insert_one(data)    

if __name__ == '__main__':
    load_all()