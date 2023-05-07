"""
Iterando strings com while
"""
#         012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#       1110987654321

nome = input('digite seu nome: ')
contador = 0
nom = ''
print(len(nome))
while contador < len(nome):
    letra = nome[contador]
    nom += f'*{letra}'
    contador += 1

nom += '*'
print(nom)
