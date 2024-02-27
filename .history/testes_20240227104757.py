import requests

def get_imdb_info(movie_name):
    url = "https://imdb8.p.rapidapi.com/title/find"
    querystring = {"q": movie_name}

    headers = {
        'x-rapidapi-key': "40d79ce6f4msh6893b4dcc8e3457p188914jsn0bb67db95879",
        'x-rapidapi-host': "moviesdatabase.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    if 'results' in data and data['results']:
        # Obtém o primeiro resultado da pesquisa
        result = data['results'][0]
        
        # Obtém o ID do título
        title_id = result.get('id')
        
        # Obtém as informações do título usando o ID do título
        info_url = f"https://imdb8.p.rapidapi.com/title/get-details?tconst={title_id}"
        info_response = requests.get(info_url, headers=headers)
        info_data = info_response.json()
        
        # Extrai informações relevantes
        title = info_data['title']['title']
        year = info_data['title']['year']
        genres = info_data['title']['genres']
        directors = [person['name'] for person in info_data['crewSummary']['directors']]
        
        return {
            'title': title,
            'year': year,
            'genres': genres,
            'directors': directors
        }
    else:
        return None

# Teste
movie_name = "La La Land"
movie_info = get_imdb_info(movie_name)

if movie_info:
    print("Informações do filme:")
    print(f"Título: {movie_info['title']}")
    print(f"Ano: {movie_info['year']}")
    print(f"Gêneros: {', '.join(movie_info['genres'])}")
    print(f"Diretores: {', '.join(movie_info['directors'])}")
else:
    print("Filme não encontrado.")
