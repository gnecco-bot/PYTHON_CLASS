# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# Self sempre tera que ter dentro da funcao da class
# Self se tornará a variavel que eu jogar a class
# exemplo: 
# class teste:
#   def __init__(self):
#       ...
# 
# variavel = teste()
# "self = variavel = self

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()