import requests

def fetch_data(endpoint, filter={}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filter)
    return response.json() if response.status_code == 200 else None

# Buscar personagens com nome "Rick"
characters_data = fetch_data("character", {'name': 'Rick'})

if characters_data and 'results' in characters_data:
    print(f"Total encontrado: {characters_data['info']['count']}\n")
    for character in characters_data['results']:
        print(f"Nome   : {character['name']}")
        print(f"Status : {character['status']}")
        print(f"Espécie: {character['species']}") 
        print(f"Origem : {character['origin']['name']}")
        print("-" * 30)
else:
    print('Nenhum personagem encontrado ou erro na requisição.')