import requests
import json

def filmeInfo():
    
    name = input('Digite o nome do filme: ')
    req = None 
    try:
        req = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=957bf17c&t={name}')
        info = json.loads(req.text)
    except:
        print('Erro na requisição')
        exit()

    if info['Response'] == 'False':
        print('Filme não encontrado')
        return None
    else:
        return info 

print(filmeInfo())