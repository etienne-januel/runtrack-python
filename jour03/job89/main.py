import os, re
import requests, json

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
pokedex = []
for pokemon in response.json()['results']:
  pokedex.append(pokemon['name'])

parent_dir = os.path.dirname(__file__)
f = open(parent_dir + '/../data.txt', 'r')
data = f.read()

for word in re.findall(r'[a-zA-Z]\w+', data):
  if word in pokedex:
    print('Magicarpe utilise Trempette', word.capitalize(), 'est K.O !')