import requests
import pytest

def test_status_code_trainers_list():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_id_in_response():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 2090})
    assert response.json()['trainer_name'] == 'Eldee' 