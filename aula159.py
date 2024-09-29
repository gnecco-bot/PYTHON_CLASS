# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass,  asdict, astuple, field #field configura campos na dataclass, tornando dados em diferentes tipos padrão
 
# @dataclass(init=False) configuração de inicialização da dataclasse
@dataclass
class Pessoa:
    # apenas dados imutáveis aceita valores padrão
    nome: str = 'Missing'
    sobrenome: str = 'not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)
        # não é compativel colocar dados mutáveis, sendo necessário ajuda do field

    # def __post_init__(self): # sempre executado pós __init__
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':
    # p1 = Pessoa('Luiz', 30)
    # p2 = Pessoa('Luiz', 30)
    # print(p1 == p2)
    p1 = Pessoa('Luiz', 'Otávio')
    # p1.nome_completo = 'Maria Helena Figueredo Alves de Lima'
    print(p1)
    # print(p1.nome_completo)
    print(asdict(p1))
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(astuple(p1))
