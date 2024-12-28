# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data = datetime.now()
print(data.timestamp()) # diz quantos segundos de 1977 até hoje
print(datetime.fromtimestamp(1735343838.633918))

data = datetime.now(timezone('America/Sao_Paulo'))
print(data)

# formata a hora em sequecia predefinida (não no tela)
# data_str_data = '2024-05-21 05:29:42
# data_str_data = '20/01/2025'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'S
# data_str_fmt = '%d/%m/%Y'
# data = datetime.strptime(data_str_data, data_str_fmt)

data = datetime(2024, 4, 1, 6, 45, 21, tzinfo=timezone('Asia/Tokyo'))
print(data) 

