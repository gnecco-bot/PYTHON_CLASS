"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

"""
try:
    numero_int = input('Digite um numero: ')
    numero_int = int(numero_int)
    numero_int = numero_int % 2
    if numero_int == 0:
        print('Esse numero é par')
    else:
        print('Esse número é impar')
except:
    print('não é um numero')
"""


"""
hora = input('Digite que horas são: ')

if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Você digitou a hora errada')
else:
    print('isso não é a "hora"')
"""


""" 
nome = input('Digite seu nome: ')
nome = len(nome)
if nome <= 4:
    print('Seu nome é muito curto')
elif nome >= 5 and nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
"""