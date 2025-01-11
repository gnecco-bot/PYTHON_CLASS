# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger # Leitor de PDF/ Escritor de PDF/ 

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdf_original'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos' 

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf' # Pasta onde está o PDF

PASTA_NOVA.mkdir(exist_ok=True) # Cria uma nova pasta / se verdadeiro não criar

reader = PdfReader(RELATORIO_BACEN) # Faz a leitura do arquivo PDF

# print(len(reader.pages)) # Quantidade de paginas no PDF
# for page in reader.pages: # Le página por página e retorna em byte
#     print(page)
#     print()

page0 = reader.pages[0] # Página no ínidice zero
imagem0 = page0.images[0] # Puxar a imagem do índice zero da pagina do índice zero

# print(page0.extract_text()) # Faz a leitura do pdf
# print(page0.images) # Retorna a imagem em bytes e seu tamnaho 

with open(PASTA_NOVA / imagem0.name, 'wb') as arquivo: # Lugar onde será salvo / Leitura no modo Write-byte
    arquivo.write(imagem0.data) # Salvar apenas a imagem do índice zero na pasta nova

writer = PdfWriter() # Modo escrita

with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo: # Clona o PDF para outra pasta
    for page in reader.pages:
        writer.add_page(page)
    
    writer.write(arquivo)

for i, page in enumerate(reader.pages): # Cria cada uma página por vez em um PDF novo 
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)


files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()

# with open()

