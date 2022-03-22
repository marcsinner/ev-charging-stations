from email import header
import requests

API_ID ="FLtUWhI-BtJ49HP5HSImgA"
API_KEY = "mXhKRWb7NSmoATA94gCPigGCiDwLrH6jY2nPnbZIv2O56LhyCq0mhoWArKiXYi7Wj3afgmbni5W4XPJku6OqIQ"
TOKEN = "GkjIczA5uhDJwiWYYI2ceDq3sqC1cqjmZwrEtnrc-gI"

r = requests.get("https://ev-v2.cc.api.here.com/ev/ev/stations.json?prox=52.516667,13.383333,5000&connectortype=31", 
headers={'Authorization' : 'Bearer: '+TOKEN})

