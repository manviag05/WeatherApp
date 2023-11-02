import requests
import json
city=input("Enter name of city : ")
url = f"https://api.weatherapi.com/v1/current.json?key=96afb82be3e64beb8ae74008230211&q={city}"
r = requests.get(url)

wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])