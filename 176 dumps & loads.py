# json.dumps e json.loads com strings + typing.TypedDict
# dump = joga o arquivo
# load = carrega o arquivo
# dumps e dump são diferente, o S no final são para trabalhar com strings
# já dump para arquivos
# Ao converter de Python para JSON:
#
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
from pprint import pprint # print na tela mais legivel
from typing import TypedDict # typagem de dicionario

class Movie(TypedDict): # typando o arquivo json para python
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
  }
  '''
filme: Movie = json.loads(string_json)
# pprint(filme, width=40)
# print()
# print(filme['title'])
# print(filme['characters'][0])
# print(filme['year'] + 10)
json_string = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_string)
