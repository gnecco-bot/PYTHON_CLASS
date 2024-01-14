# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def addlista(tarefa1, lista=None):
    if lista is None:
        lista = []
    lista.append(tarefa1)
    return lista

tarefa = addlista('')
historico = []

while True:
    print('Comandos: listar, desfazer, refazer')
    resposta = input('Digite uma tarefa ou comando: ')

    resposta_up = resposta.upper()

    if resposta_up == 'LISTAR' or 'REFAZER' or 'DESFAZER':
        if resposta_up == 'LISTAR':
            for i in tarefa:
               print(i)
            print('')
            continue

        if resposta_up == 'DESFAZER':
            historico.append(tarefa[-1])            
            del(tarefa[-1])
            for i in tarefa:
                print(i)
            print('')
            continue

        if resposta_up == 'REFAZER':
            tarefa.append(historico[-1])
            del(historico[-1])
            for i in tarefa:
                print(i)
            print('')
            continue

    addlista(resposta, tarefa)
    print('')
    print(resposta)
    print('')
