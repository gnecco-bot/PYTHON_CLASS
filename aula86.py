produtos = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'escritorio',
}

print(produtos.items())

for chave, valor in produtos.items():
    print(chave, valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produtos.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

dc1 = {
    chave: valor
    for chave, valor in lista
}

print(dc) 
print(dc1)

s1 = {2 ** i for i in range(10)}
# print(set(range(10)))
print(s1)