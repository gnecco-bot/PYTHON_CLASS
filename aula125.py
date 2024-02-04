# Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

# Pessoa.ano_atual = 1 
# modifica o valor da class inteira
# isso apenas para variavel dentro de class
# self.ano_atual = 1
# modifica apenas o valor da instancia
# valor da classe permanece o mesmo
# instancia é a variavel em que jogou a class
# self dentro de class se categoriza como a variavel
# na qual posso fazer manipulações 