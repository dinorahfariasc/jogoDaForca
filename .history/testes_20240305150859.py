import requests
import json

req = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=957bf17c&t=the+handmaiden')

print(req.text)