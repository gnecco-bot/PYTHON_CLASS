# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
# p1 = Pessoa('João', 35)
# p1.nome = 'EITA'
# print(p1.idade)

p1.__dict__['outra'] = 'coisa'
# direto na classe nao adiciona
# mas na instancia consigo adicionar outro dict
#
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
print(vars(p1))
print(p1.nome)