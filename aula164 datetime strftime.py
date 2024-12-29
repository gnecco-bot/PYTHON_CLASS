# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2024-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt)) # formata para a sequencia de data preferida
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y %H:%M:%S'))
print(data.strftime('%d'), data.day) # string / inteiro
print(data.strftime('%m'), data.month) # string / inteiro
print(data.strftime('%Y'), data.year) # string / inteiro 
print(data.strftime('%H'), data.hour) # string / inteiro
print(data.strftime('%M'), data.minute) # string / inteiro 
print(data.strftime('%S'), data.second) # string / inteiro
