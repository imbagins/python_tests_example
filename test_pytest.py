from multiprocessing import Value
import requests
import pytest


def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200


def test_name_trainer ():
    response_name_trainer = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':'1157'})
    assert response_name_trainer.json()['trainer_name'] == 'Эшли'


def test_addpok ():
    response_addpok = requests.post('https://pokemonbattle.me:5000/trainers', params={'pokemon_id':'1461'})
    assert response_addpok.json()['message'] == 'Неверный токен'


@pytest.mark.parametrize('key, value', [('trainer_name', 'Эшли'),('city', 'Анапа')])

def test_param(key, value):
    response_param=requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id':'1157'})
    assert response_param.json()[key] == value