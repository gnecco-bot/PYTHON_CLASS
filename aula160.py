# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm

#namedtuple são classes com apenas valores(atributos) sem executar nenhum método, são perfeitas para criar dados sem a necessidade de uma estrutura class padrão 

from collections import namedtuple
from typing import NamedTuple

# SEGUNDO METODO (FUNCIONA DO MESMO JEITO) VANTAGEM: PODE TYPAR OS ATRIBUTOS DEIXANDO MAIS COMPREENSIVEL
# class Carta(NamedTuple):
#     valor: str = 'VALOR'
#     naipe: str = 'NAIPE'

# PRIMEIRO METODO
Carta = namedtuple(
    'Carta', ['valor', 'naipe'],
    defaults=['VALOR', 'NAIPE']                   
)
as_espadas = Carta('A', '♠️')

print(as_espadas)
print(as_espadas.valor)
print(as_espadas[0])
print(as_espadas.naipe)
print(as_espadas[1])
print()
print(as_espadas._fields)
print(as_espadas._field_defaults)
print(as_espadas._asdict())
print()

for valor in as_espadas:
    print(valor)