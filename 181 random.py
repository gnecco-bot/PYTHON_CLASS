# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random
import time

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(7) # seed é um numero usado para gerar uma nova sequencia, repetir o numero repete a sequência
random.seed(time.time())
print(time.time())

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print('Range:', r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print('Randint:', r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print('Uniform:', r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
print('Shuffle:', random.shuffle(nomes))

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
print('Sample:', novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print('Choices:', novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print('Choice:', random.choice(nomes))
