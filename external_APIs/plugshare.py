import requests
import cfscrape

TOKEN = "d2ViX3YyOkVOanNuUE54NHhXeHVkODU="
url= "https://api.plugshare.com/v3/locations/region?access=1&cost=true&count=500&include_coming_soon=true&latitude=50.93565112181302&longitude=6.9217833676119955&minimal=0&spanLat=0.12213496654899814&spanLng=0.26058197021484375"

url_auth = url+"?Authorization='Basic d2ViX3YyOkVOanNuUE54NHhXeHVkODU='"

r = requests.get(url,
headers={'Authorization' : 'Basic: '+TOKEN})

session = requests.session()
session.headers = {'Authorization' : 'Basic: '+TOKEN}
scraper = cfscrape.create_scraper(sess=session)

#Method 1
scraper = cfscrape.create_scraper()
print(scraper.get("https://www.plugshare.com/location/36914").content)

# Method 2
r = requests.get("https://www.plugshare.com/location/36914")
print(r)


