# Classes decoradoras (Decorador classes)

class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwargs): # valores que são entrados são do 
        print(*args, **kwargs) # retorno da soma() que será sobrescrevido
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador

@Multiplicar
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2,4)
print(dois_mais_quatro)
print('Primeira maneira')
print()

# segunda maneira
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        print(func) # retorna a funcao
        def interna(*args, **kwargs): # retorna os parametros da funcao
            print(*args, **kwargs)
            resultado = func(*args, **kwargs) # executa a funcao soma
            print(resultado) 
            return resultado * self._multiplicador # multiplica por 2 a funcao soma
        return interna

@Multiplicar(2) # exe a func 2x por conta do __call__, no __init__ deve ser declarado o parametro que entrara no decorador
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2,4)
print(dois_mais_quatro)