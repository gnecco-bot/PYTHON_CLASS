# sys.argv - Executando arquivos com argumentos no sistema
# sys.argv: informa quantos argumentos você está dando para o python executar 
# na linha de comando do terminal
import sys

argumentos = sys.argv # 
qtd_argumentos = len(argumentos) # conta quantos argumentos foi passado (é salvo em lista)

print(sys.argv) # printa na tela a lista de argumentos passado
 
if qtd_argumentos <= 1: # se passado apenas um argumento faça
    print('Você não passou argumentos')
else: # senão
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com "{argumentos[1:]}"')
        print(f'Faça outra coisa com "{argumentos[2:]}"')
        print(f'Faça outra coisa com "{argumentos[3:]}"')
    except IndexError:
        print('Faltam argumentos')