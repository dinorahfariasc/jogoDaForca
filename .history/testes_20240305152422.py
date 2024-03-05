import requests
import json

name = input('Digite o nome do filme: ')

req = none 
try:
    req = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=957bf17c&t={name}')
    info = json.loads(req.text)
except:
    print('Erro na requisição')
    exit()

print(info)