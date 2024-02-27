import requests
from bs4 import BeautifulSoup

def get_imdb_info(movie_name):
    # Pesquisar o filme na API do IMDb
    search_url = f"https://www.imdb.com/find?q={movie_name}&s=tt&ttype=ft&ref_=fn_ft"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extrair o link do filme
    try:
        movie_link = soup.find('td', class_='result_text').find('a')['href']
    except AttributeError:
        return None
    
    # Acessar a página do filme
    movie_url = f"https://www.imdb.com{movie_link}"
    movie_response = requests.get(movie_url)
    movie_soup = BeautifulSoup(movie_response.text, 'html.parser')
    
    # Extrair informações do filme
    title = movie_soup.find('div', class_='title_wrapper').find('h1').text.strip()
    try:
        year = movie_soup.find('span', id='titleYear').find('a').text
    except AttributeError:
        year = "N/A"
    genre = [genre.text.strip() for genre in movie_soup.find('div', class_='subtext').find_all('a', {'title': None})]
    try:
        director = movie_soup.find('div', class_='credit_summary_item').find('a').text
    except AttributeError:
        director = "N/A"
    
    return {
        'title': title,
        'year': year,
        'genre': genre,
        'director': director
    }

# Teste
movie_name = "La La Land"
movie_info = get_imdb_info(movie_name)

if movie_info:
    print("Informações do filme:")
    print(f"Título: {movie_info['title']}")
    print(f"Ano: {movie_info['year']}")
    print(f"Gênero: {', '.join(movie_info['genre'])}")
    print(f"Diretor: {movie_info['director']}")
else:
    print("Filme não encontrado.")
