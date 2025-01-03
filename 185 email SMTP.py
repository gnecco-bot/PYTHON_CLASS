# Enviando E-mails SMTP com Python

import os # acessa partes as variaveis de ambiente exportada pelo load_dotenv
from dotenv import load_dotenv # carregar todas as variaves de ambiente
import pathlib # acessar documento 

from string import Template # substituir strings no documento

from email.mime.multipart import MIMEMultipart # preenche as partes do email, titulo, assunto, etc
from email.mime.text import MIMEText # formata o texto do email com extensao de arquivo, etc

import smtplib # abre conexão com o server

load_dotenv() # carrega as variaveis do ambiente

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / '185.html' # caminho do arquivo que sera enviado

# Dados do rementente e destinatário
remetente = os.getenv('FROM_EMAIL', '') # leitura da variavel de ambiente
destinatario = remetente # destinatario é o mesmo que o remetente

# Configurações SMTP
smtp_server = 'smtp.gmail.com' # conexão do server
smtp_port = 587 # porta
smtp_username = os.getenv('FROM_EMAIL', '') # variavel de email do ambiente
smtp_password = os.getenv('EMAIL_PASSWORD', '') # variavel de senha do ambiente

# Mensagem de texto
with open(CAMINHO_HTML, 'r') as arquivo: # abre o arquivo e sobre escreve as strings
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João') # nome sera preenchido com 'Joao'

# print(texto_email)

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email) # anexar o texto com extensão com as partes do email formatado

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo() # verificação se conexão
    server.starttls() # protocolos
    server.login(smtp_username, smtp_password) # login
    server.send_message(mime_multipart) # email formatado
    print('E-mail enviado com sucesso!') # envio com sucesso

