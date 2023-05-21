perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1','3','4','5'],
        'Resposta' : '4',    
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['25','55','10','51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['4','5','2','1'],
        'Resposta' : '5',
    },
]

acertos = 0

print('Pergunta:', perguntas[0]['Pergunta'])
print()
print('Opções:')

i = 0
for opc in perguntas[0]['Opções']:
    print(f'{i})',opc)
    i += 1

res = input('Escolha uma opção: ')
try:
    if perguntas[0]['Resposta'] == perguntas[0]['Opções'][int(res)]: 
        print('Acertou 👍')
        acertos += 1
    else:
           print('Errou ❌')
except:
    print('Errou ❌')

print() 

print('Pergunta:', perguntas[1]['Pergunta'])
print()
print('Opções:')

i = 0
for opc in perguntas[1]['Opções']:
    print(f'{i})',opc)
    i += 1

res = input('Escolha uma opção: ')
try:
    if perguntas[1]['Resposta'] == perguntas[1]['Opções'][int(res)]: 
        print('Acertou 👍')
        acertos += 1
    else:
        print('Errou ❌')
except:
    print('Errou ❌')

print() 

print('Pergunta:', perguntas[2]['Pergunta'])
print()
print('Opções:')

i = 0
for opc in perguntas[2]['Opções']:
    print(f'{i})',opc)
    i += 1

res = input('Escolha uma opção: ')
try:
    if perguntas[2]['Resposta'] == perguntas[2]['Opções'][int(res)]: 
        print('Acertou 👍')
        acertos += 1
    else:
        print('Errou ❌')
except:
    print('Errou ❌')

print()
print('Você acertou', acertos)
print('de 3 perguntas.')
print()

