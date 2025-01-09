# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

import subprocess
import sys

print(sys.platform) # Retorna o sistema que está sendo executado o script

cmd = ['ping', '127.0.0.1', '-c', '4'] # Comando para pingar 4 vezes no linux/mac
enconding = 'utf-8' # Codificação linux/mac
system = sys.platform # Retorna o sistema operacional

if system == 'win32':
    cmd = ['ping', '127.0.0.1'] # Comando para ping na rede local
    encoding = 'cp850' # Codificador


proc = subprocess.run(
    cmd, capture_output=True, # Executa o comando passado em cmd + capturação de resposta ativo (jogavel em uma variavel)
    text=True, encoding=encoding # Codifica a resposta do terminal 
)

print()

# print(proc.args) # Retorna a lista dos argumentos passado para o terminal
# print(proc.stderr) #
print(proc.stdout) # Retorna em bytes a resposta do comando
# print(proc.stdout.decode('cp850')) # Retorna codificado
# print(proc.returncode) # Retorna a comunicação se foi bem sucessedida (0=OK)