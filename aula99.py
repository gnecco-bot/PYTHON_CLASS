from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import soma_do_modulo, fala_oi
# from aula99_package.modulo import *


print(soma_do_modulo(4,8))
print(modulo.soma_do_modulo(9,3))
print(aula99_package.modulo.soma_do_modulo(5,5))
# print(variavel)
# print(nova_variavel)
fala_oi()
# print(__name__)
# print(*path, sep='\n')