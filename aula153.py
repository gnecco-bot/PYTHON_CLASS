# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print(*args, *kwargs, 'está chamando', self.phone)
        return 'valor do retorno'

call1 = CallMe('123123')
retorno = call1('Alguém')
print(retorno)