# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
# new é a super classe que vem antes do init
# new e init sempre é iniciado quando se cria uma instancia


class A(object):
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois')
        instancia.x = 'instancia do new'
        return instancia

    def __init__(self, y):
        self.y = y
        print('Sou o init')

    def __repr__(self) -> str:
        return 'A()'
    
# a = object.__new__(A)
# a.__init__()
a = A('segundo parametro')
print(a)
print(a.x)
print(a.y)