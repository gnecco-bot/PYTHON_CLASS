def multiplicacao(*args):
    total = 1
    for numeros in args:
        if numeros == 0:
            total = 1 * total
        else:
            total = numeros * total
    return total

print(multiplicacao(2,4,6,8))

def par_impar(num):
    num = num % 2
    if num == 0:
        return 'par'
    return 'impar'

print(par_impar(2131235))