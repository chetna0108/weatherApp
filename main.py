import requests
import json
import os

city=input("enter the name of the city :")
url="http://api.weatherapi.com/v1/current.ison?key=b13989793f184149a91141538230103&q={city}"
r=requests.get(url)
print(r.text)
wdic =json.loads(r.text)
w= wdic["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {w} degree.'")