# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
# delimitador de chaves é codificado por padrão com sifrão "$"

import locale
import string
from datetime import datetime
from pathlib import Path
import json

CAMINHO_ARQUIVO = Path(__file__).parent / '183.txt' # volta uma pasta e acessa o arquivo 183.txt

locale.setlocale(locale.LC_ALL, '') # localidade mudado para a padrão do sistema

def converte_para_brl(numero: float) -> str: # retorna formatado para dinheiro br
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

print(json.dumps(dados, indent=2, ensure_ascii=False)) # exibe na tela de maneira mais legivel

# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

# Atenciosamente,

# ${empresa}, 
# Abraços
# '''
# template = string.Template(texto)
# print(template.substitute(dados))

class MyTemplate(string.Template): # muda o delimitador para um codificador predefinido
    delimiter = '%'

with open(CAMINHO_ARQUIVO, 'r') as arquivo: # faz a leitura do arquivo substituindo as chaves
    texto = arquivo.read()
    # template = string.Template(texto)
    template = MyTemplate(texto)
    print(template.substitute(dados))
    # print(template.safe_substitute(dados)) # não da erro na tela msm faltando chaves