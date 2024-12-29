# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree 
# Apagar Árvore recursivamente -> shutil.rmtree # não vai para a lixeira
# Apagar arquivos -> os.unlink
# Renomear/Mover (é a mesma coisa) -> shutil.move ou os.rename

import os
import shutil

IMAGEM = os.path.join('d:\\', 'usuario', 'imagens')
PASTA_ORIGINAL = os.path.join(IMAGEM, 'edit')
NOVA_PASTA = os.path.join(IMAGEM, 'NOVA_PASTA')

# os.unlink(NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True) # remove a arvore da pasta
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA) # copia a arvore da pasta
# shutil.rmtree(NOVA_PASTA, ignore_errors=True) 
shutil.move(NOVA_PASTA, NOVA_PASTA + '_NOVO_NOME')