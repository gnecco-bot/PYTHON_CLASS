# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)

teste2 = 'teste'
teste = Carro(teste2)
teste.acelerar()
Carro.acelerar(teste)

nome = 'a'
print(f'lugar na memoria:{fusca=}')
print(f'exibe o nome da variavel + o valor {nome=}')