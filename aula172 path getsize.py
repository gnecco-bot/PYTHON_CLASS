# os.path.getsize e os.stat para dados dos arquivos
import math
import os
from itertools import count

def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

print(formata_tamanho(1000))
print(formata_tamanho(1000000))
print(formata_tamanho(1000000000))
print(formata_tamanho(1000000000000))


caminho = os.path.join('d:\\', 'Usuario', 'imagens')
counter = count()

for root, dirs, files in os.walk(caminho): # pasta | subdiretorios | arquivos
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_completo_arquivo)
        print('  ', the_counter, 'File:', file_, formata_tamanho(tamanho))

        stats = os.stat(caminho_completo_arquivo)
        tamanho2 = stats.st_size
        print('  ', the_counter, 'com stats:', file_, formata_tamanho(tamanho2))
        print()
