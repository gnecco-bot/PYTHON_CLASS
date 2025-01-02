# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / '178-ex.csv'
print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo) # le o arquivo CSV em modo dicionario

    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereco'])
        print(linha)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo) # le o arquivo CSV em modo lista

    for linha in leitor:
        # print(linha[0], linha[1], linha[2])
        print(linha)
