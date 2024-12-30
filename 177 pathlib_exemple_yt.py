from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
# print(caminho_projeto.absolute()) # retorna o caminhao absoluto

caminho_arquivo = Path(__file__)
print(caminho_arquivo) # caminho completo do arquivo

print(caminho_arquivo.parent.parent.parent) # retorna uma pasta

ideias = caminho_arquivo.parent / 'ideias' # volta uma pasta e acessa outra
print(ideias / 'arquivos.txt') 

print(Path.home()) # retorna o caminho do usuario

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch() # cria o arquivo
print(arquivo)
arquivo.write_text('Olá mundo') # escreve no arquivo, apenas o ultimo comendo write sera salvo
print(arquivo.read_text())
arquivo.write_text('') # nao passando nada, apaga os dados escritos no arquivo

with arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('outra linha\n')

print(arquivo.read_text())

caminho_pasta = Path.home() / 'desktop' / 'python é legal'
caminho_pasta.mkdir(exist_ok=True) # cria uma pasta
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True) # cria uma pasta

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch() # cria o arquivo
outro_arquivo.write_text('Heey') # escreve no arquivo

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch() # cria o arquivo
mais_arquivo.write_text('Heey') # escreve no arquivo

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'files_{i}.txt' # cria 10 arquivos txt
    file.touch() # cria os arquivos
    if file.exists(): # verifica se existe o arquivo
        file.unlink() # apaga os arquivos
    else:
        file.touch() # cria os arquivos

    with file.open('a+') as text_file:
        text_file.write('Olá Mundo\n')
        text_file.write(f'file_{i}.txt')

# rmtree(caminho_pasta) # apaga a pasta e suas sub pasta

def rmtree(root: Path, remove_root=True): # remover o diretorio e suas sub pasta
    for file in root.glob('*'): # for in toda as pastas root
        if file.is_dir(): # se root for diretorio
            print('DIR: ', file) # joga na tela a iteração do diretorio atual 
            rmtree(file, False) # chama de novo a função (recursiva)
            file.rmdir() # remove o diretorio quando a recursiva for satisfeita
        else:
            file.unlink() # remove o arquivo
            print('FILE: ', file) # joga na tela o arquivo removido
    
    if remove_root: # quando sair da recursiva se torna True
        root.rmdir() # remove a pasta root

rmtree(caminho_pasta)