# requests para requisições HTTP
import requests

# portas padrões quando não informado uma porta específica
# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/' 
response = requests.get(url) # faz a leitura do site

print(response) # Retorna o status do servidor
print(response.status_code) # Status da comunicação com o servidor
print(response.headers) # Cabeçalho do site
# print(response.content) # Retorna o conteudo em modo byte
print(response.text) # Retorna o texto html do site mais legível
# print(response.json()) # Retorna arquivo json
