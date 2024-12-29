# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('d:\\', 'Usuario', 'imagens')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    # print(caminho_completo_pasta)

    if not os.path.isdir(caminho_completo_pasta): # se nao for um diretorio continue
        continue
    
    print(pasta)

    for imagem in os.listdir(caminho_completo_pasta): # se for, expandir e printar
        print('  ', imagem)