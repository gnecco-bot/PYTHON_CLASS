# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Dotenv: é uma biblioteca que permite o acesso as variaveis de ambiente para armazenar e acessar
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
# import os

# senha = os.getenv('VARIAVEL') # criado uma variavel em tempo de execução no terminal

# print(senha)

from dotenv import load_dotenv # type: ignore
import os

load_dotenv() # Carrega todas as variaveis do ambiente 

# print(os.environ)
print(os.getenv('BD_USER'))
print(os.getenv('BD_PASSWORD'))
print(os.getenv('BD_PORT'))
print(os.getenv('BD_HOST'))

# Arquivo .env nao pode ter nenhum nome além da extensão