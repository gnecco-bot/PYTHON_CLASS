# secrets gera números aleatórios seguros
import secrets
import time
import string as s
from secrets import SystemRandom as Sr

print('Gerar senha de 12 caractéres:', ''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))

# para executar em linha de comando (cmd ou terminal)
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"

random = secrets.SystemRandom()

# print(secrets.randbelow(100)) # gera um numero aleatorio abaixo de 100
# print(secrets.choice([1,51,31,86])) # escolhe apenas um desta lista

# Funções:
# seed
#   -> EM SECRETS SEED NAO AFETA NAO SE DA PARA CONTROLAR
random.seed(time.time())
print(time.time())

# random.randrange(início, fim, passo)}
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

