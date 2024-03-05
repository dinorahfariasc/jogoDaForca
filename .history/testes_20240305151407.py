import requests
import json

name = input('Digite o nome do filme: ')

req = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=957bf17c&t={name}')

print(req.json())