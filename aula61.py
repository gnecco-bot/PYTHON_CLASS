"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""


cpf_envio = '55417963852'
# pega_nove = cpf.split('-')
# nove_digito = pega_nove[0].split('.')
nove_digito = cpf_envio[:9] 
regressivo1 = 10
valor_total1 = 0

for i in nove_digito:
    valor_total1 += int(i) * regressivo1
    regressivo1 -= 1

primeiro_digito = valor_total1 * 10 % 11 
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digito = nove_digito + str(primeiro_digito)
regressivo2 = 11
valor_total2 = 0

for soma in dez_digito:
    valor_total2 += int(soma) * regressivo2
    regressivo2 -= 1

segundo_digito = valor_total2 * 10 % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digito}{primeiro_digito}{segundo_digito}'

if cpf_envio == cpf_gerado:
    print(f'Esse CPF {cpf_envio} é válido.')
else:
    print('CPF inválido.')


 