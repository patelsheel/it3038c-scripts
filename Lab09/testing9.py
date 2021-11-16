import requests
import json

r = requests.get("http://localhost:3000")
data = r.json()

print(data)

i = 0
while i < len(data):
    i = i + 1
    print(data[i - 1]['name'] + ' is ' + data[i - 1]['color'])
