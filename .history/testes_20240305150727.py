import requests
import json

req = requests.get('http://www.omdbapi.com/?apikey=[957bf17c]&')

print(req.text)