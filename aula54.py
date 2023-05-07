import os

lista_compras = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        compras = input('Valor: ')
        if compras != '':
            lista_compras.append(compras)
        else:
            print('Você não adicionou um valor.')

    if opcao == 'a':
        try:
            indice = int(input('Escolha a índice para apagar: '))
            if indice != '':
                del lista_compras[indice]
            else:
                print('Campos vazios.')
        except:
            print('Você não digitou um número ou você digitou uma índice maior do que realmente tem.')
    
    if opcao == 'l':
        os.system('cls')
        if lista_compras != []:
            for i, p in enumerate(lista_compras):
                print(i, p)
        else:
            print('Não tem nada na lista.')
        



        