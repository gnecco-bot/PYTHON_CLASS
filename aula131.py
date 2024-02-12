# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# assim de vez colocar () para executar o método
# pode se utilizar apenas o nome, parecerá que trabalhará
# como atributo mas irá está trabalhando com método
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente ex: mudar atributo no programa do cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)
print(caneta.cor_tampa)

#####################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor
#         # self.cor = cor
    
#     def get_cor(self):
#         return self.cor_tinta

# caneta = Caneta('Azul')
# # print(caneta.cor)
# # print(caneta.cor)
# # print(caneta.cor)
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
