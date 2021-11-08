import requests
import json

print('Please enter a zip code:')

zip = input()

r = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=74f68dae8e0afb05e1a44c5b86cc8ae3' % zip)
data = r.json()

print(type(data['weather'][0]['description']))
print('The weather in %s is %s' % (zip, data['weather'][0]['description']))
