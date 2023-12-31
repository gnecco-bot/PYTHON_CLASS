"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

lista_soma = []
for i in range(len(l2)):
    lista_soma.append(l1[i] + l2[i])

lista_soma_2 = [x + y for x, y in zip(l1, l2)]

def somatoria (l1, l2):
    lista_menor = min(len(l1), len(l2))
    return [
        l1[i] + l2[i] for i in range(lista_menor)
    ]

print(lista_soma,'lista_soma')
print(lista_soma_2,'lista soma 2')
print(somatoria(l1, l2))
