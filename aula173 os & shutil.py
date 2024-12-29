# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

# HOME = os.path.expanduser('~') # retorna o caminho do usuario
IMAGEM = os.path.join('d:\\', 'usuario', 'imagens')
# DESKTOP = os.path.join(IMAGEM, 'Desktop')
PASTA_ORIGINAL = os.path.join(IMAGEM, 'edit')
NOVA_PASTA = os.path.join(IMAGEM, 'NOVA_PASTA')
print(NOVA_PASTA)

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        print(caminho_novo_diretorio)
        os.makedirs(caminho_novo_diretorio, exist_ok=True) # cria pasta
    
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo) # copia de arquivo
        