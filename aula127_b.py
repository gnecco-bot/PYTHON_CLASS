import json
from aula127 import CAMINHO_ARQUIVO, Pessoa, fazer_dump

fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    
    print(p1.nome)
    print(p2.nome)
    print(p3.nome)

print(__name__)