# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / '186_diretorio_zip' # Pasta raiz/diretorio
CAMINHO_COMPACTADO = CAMINHO_RAIZ / '186_compactado.zip' # Pasta raiz/compactado
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / '186_descompactado' # Pasta raiz descompactada

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True) # Remova toda a árvore da pasta diretorio
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)  # Apaga o arquivo compactado
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True) # Renomeia o .zip para "" 
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True) # Remove toda a árvore do arquivo descompactado 

# raise Exception() # lança uma exceção

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

# Cria arquivos
def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo: # for de quantos arquivos será criado
            arquivo.write(texto) # escrevendo no diretorio arquivos

criar_arquivos(10, CAMINHO_ZIP_DIR) # quantos arquivos | diretorio onde salvo

# Compactando os arquivos do diretório
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip: 
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file) # Escreve no caminho o arquivo de índice do range

# Lendo o arquivo zip sem descompactar pelo sistema
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip: 
    for arquivo in zip.namelist():
        print(arquivo)

# Descompacta o arquivo compactado para a pasta descompactada
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip: 
    zip.extractall(CAMINHO_DESCOMPACTADO)