import requests
import json

req = requests.get('http://www.omdbapi.com/?apikey=[957bf17c]&t=the+handmaiden')

print(req.text)