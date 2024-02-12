# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primiero
# parâmetro, recebermos a prória classe. 

class Pessoa:
    ano = 2023 # atributo de calsse

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
        
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)
            
    @classmethod
    def criar_sem_nome_e_idade(cls):
        return cls('Anônimo', 19)

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônimo', 34)
p4 = Pessoa.criar_sem_nome(25)
p5 = Pessoa.criar_sem_nome_e_idade()
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
print(p5.nome, p5.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()