# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         print('DEPOIS DO UPPER')
#         return retorno
    
# string = MinhaString('Luiz')
# print(string.upper()) # Este upper é do def em que criei

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        print('Ei, Burlei o sitema.')

    def metodo(self):
        super(B, self).metodo() # A
        super().metodo() # B super(C, self).metodo()
        print('C (acima super)')
        print()
        A.metodo(self)
        B.metodo(self)
        print('C (acima chamando pela classe)')

print()
a = A('atributo a')
print(a.atributo_a)
print()
print(a.atributo)
b = B('atributo b', 'qualquer coisa b')
print()
print(b.atributo_a)
print(b.atributo_b)
print()
print(b.atributo)
print(b.outra_coisa)
print()
c = C('atributo c','qualquer coisa c')
print()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print()
c.metodo()
print()
print(c.atributo)
print(c.outra_coisa)
print()


# O que tem no A, é apenas oque tem no A por não fazer herança
# No B, tem o A e o B, contem oque tem nos 2 por fazer herança
# No C, contem oque tem no A, B e C por fazer herança com o B