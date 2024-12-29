# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('users','teste', 'testando.txt') # junta os diretorios e arquivo
print(caminho)
diretorio, arquivo = os.path.split(caminho) # divide o diretorio e o arquivo final
print(diretorio)
print(arquivo)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho) 
print(caminho_arquivo, extensao_arquivo)

print(os.path.exists(caminho)) # retorna valores boleano
print(os.path.exists('/usuario')) # verifica se o arquivo existe
print(os.path.abspath('.')) # retorna o caminho da onde o codigo é executado
print(os.path.basename(caminho)) # retorna a parte final do caminho 
print(os.path.dirname(caminho)) # retorna apenas os diretorio (não arquivo)