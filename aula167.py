# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, '') # muda a localidade para a padrão do s.o

print(locale.getlocale()) # pega a localidade de lingua do s.o

print(calendar.calendar(2024)) # retonar o calendario de 2024