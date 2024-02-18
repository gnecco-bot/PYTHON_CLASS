# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta 

class FerramentaDeEscrever:
    def __init__(self, ferramenta):
        self.nome = ferramenta 

    def escrever(self):
        return f'{self.nome} está escrevendo'
    
escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever()) # Não tem registro de quem utilizou
print(escritor.ferramenta.escrever()) # Aponta para quem foi o usuario em que utilizou

# Não mexe na parte do usuário
# Referência para um mesmo local na memoria
# É uma Associação
# Em um sistema mais complexo, com isso você consegue registra/aponta
# a ausência de quem utilizou tal ferramenta
