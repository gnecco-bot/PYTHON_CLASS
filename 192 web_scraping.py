# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import requests # Requisições 
import re # Expressão Regulares
from bs4 import BeautifulSoup # Interpretar os dados HTML

url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text # Todo o conteudo da pagina em texto em uma variavel
parsed_hmtl = BeautifulSoup(raw_html, 'html.parser') # Feito a leitura e convertido para objeto

# print(parsed_hmtl.title) # Retorna a tag e o titulo da pagina
# print(parsed_hmtl.text) # Retorna todo o texto do site

# if parsed_hmtl.title is not None: # Title pode retorna a tag ou None
#     print(parsed_hmtl.title.text) # Retorna apenas o texto da tag title
top_jobs_heading = parsed_hmtl.select_one('#intro > div > div > article > h2') # Seleciona apenas o caminho indicado do HTML

if top_jobs_heading is not None: # Verifica se existe
    print(top_jobs_heading.text) # Imprime o caminho indicado com apenas o texto

    article = top_jobs_heading.parent # Volta uma tag 

    if article is not None: # Verifica se existe
        # print(article) # Imprime o caminho que havia voltado com a tag e todo o conteúdo dentro
        for p in article.select('p'): # Seleciona todos os parágrafos dentro de article
            # print(p.text) # Imprime o conteúdo dos parágrafos
            # print()
            print(re.sub(r'\s{1,}', ' ', p.text).strip()) # Remove todos os espaços e quebras de linhas