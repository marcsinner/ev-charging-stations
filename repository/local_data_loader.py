import json
import os

def loadLocalData(path):
    cwd = os.getcwd()

    with open(os.path.join(cwd, path)) as json_file:
        data = json.load(json_file)
        return data


def main():
    # Plugsurfing
    path = 'data\\plugsurfing_cologne.json'
    data = loadLocalData(path)
    print("loaded plugsurfing: %i" % len(data))

    path = 'data\\plugshare_cologne.json'
    data = loadLocalData(path)
    print("loaded plugshare: %i" % len(data))

    path = 'data\\placetoplug_cologne.json'
    data = loadLocalData(path)
    data = data["data"]["findChargingZones"]["chargingZones"]
    print("loaded plaetoplug: %i" % len(data))

if __name__ == '__main__':
    main()