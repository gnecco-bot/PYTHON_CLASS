# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
# Time Delta é a diferença de valores entre 2 datas

from datetime import datetime, timedelta # biblioteca de datas
from dateutil.relativedelta import relativedelta # pode fazer modificações e esclarecer diferenças de datas

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# print(data_inicio > data_fim)
# print(data_inicio < data_fim)
# print(data_inicio == data_fim)

delta = data_fim - data_inicio
print(delta)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

delta = timedelta(days=10, hours=2) # acrescenta dias e horas...
print(data_fim + delta, 'teste')

print(data_fim + relativedelta(seconds=154, minutes=604)) # acrescenta secundos e minutos

delta = relativedelta(data_fim, data_inicio) # retorna a difença entre as datas
print(delta)
print(delta.days, delta.years, delta.months)
