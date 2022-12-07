import requests
token ='9dca68a5d4716a2616a3f920a3f74a74'

response=requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    
    "name": "Леня",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"

})
print(response.text)


response_put=requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    
   "pokemon_id": 1459,
    "name": "Ленечка",
   
})
print(response_put.text)

response_post_pok=requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token': token}, json={
    
   
    "pokemon_id": "1459"

   
})
print(response_post_pok.text)