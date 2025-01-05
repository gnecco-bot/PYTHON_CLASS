# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic', # Comando a ser usado no terminal. Em ordem representa um o comando predefinido para um comando existente no ArgumentParser
    help='Mostra "olá mundo" na tela', # Comando --help mostra oq é o argumento 
    # type=str, # Tipo do argumento
    metavar='STRING', # BASIC para STRING
    # default='Olá mundo', # Valor padrão do argumento 
    required=False, # Requerimento obrigatório de valor
    action='append', # Aceita valores e argumento passados mais de uma vez (salva em lista)
    # Exemplo: clear ; python -u "d:\Usuario\Documents\PYTHON\PYTHON UDEMY\188 argparse.py" -b "a" -b "b" -b "c" 
    # nargs='+' # Aceita mais valores para um argumento só (salva em uma lista)
    # Exemplo: clear ; python -u "d:\Usuario\Documents\PYTHON\PYTHON UDEMY\188 argparse.py" -b "a" "b" "c"
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs', 
    action='store_true', # retorna valor True ou False, da para fazer checagem
)
args = parser.parse_args()
# print(args.b)

if args.basic is None:
    print('Você não passou o valor de b')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)