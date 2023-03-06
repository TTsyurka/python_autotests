import requests

url = r'https://pokemonbattle.me:9104' # использую raw string на всякий случай из-за косых, хотя вроде с этими и необязательно
trainer_token = 'f32b4af6626d6bac48db8c1775004f29'
trainer_id = 2090

# создание покемона
url_create = url + r'/pokemons'
pokemon_create_response = requests.post(url_create, headers ={'Content-Type' : 'application/json',
                                                              'trainer_token' : trainer_token},
                                                                json = {"name": "London002",
                                                                        "photo": "https://dolnikov.ru/pokemons/albums/023.png"})
print(pokemon_create_response.text)

# Смена имени покемона
url_rename = url + r'/pokemons'
pokemon_rename_response = requests.put(url_rename, headers ={'Content-Type' : 'application/json',
                                                              'trainer_token' : trainer_token},
                                                                json = {"pokemon_id": 5992,
                                                                        "name": "Paris001",
                                                                        "photo": ""})
print(pokemon_rename_response.text)

# Поймать покемона в покебол
url_catch = url + r'/trainers/add_pokeball'
pokemon_catch_response = requests.post(url_catch, headers ={'Content-Type' : 'application/json',
                                                              'trainer_token' : trainer_token},
                                                                json = {"pokemon_id": 5992})
print(pokemon_catch_response.text)

