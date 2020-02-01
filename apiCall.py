import requests
import json
baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '0885909950804'}
response = requests.get(baseURL, params=parameters)
print(response.url)
content = response.content
info = json.loads(content)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)