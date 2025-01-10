from time import sleep
from threading import Thread # Ativa o modo Thread
from threading import Lock # Trava a Thread com um laço por vez

# print('a')

# for i in range(10):
#     print(i)
#     sleep(.5)

# print('b')

# Executando Threads via Class
# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
              

# t1 = MeuThread('Thread 1', 5)
# t1.start() # Começar a thread

# t2 = MeuThread('Thread 2', 2)
# t2.start() # Começar a thread

# t3 = MeuThread('Thread 3', 3)
# t3.start() # Começar a thread

# for i in range(10):
#     print(i)
#     sleep(1)


# Outra maneira de executar threads
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('olá 1', 5))
# t1.start() # Começar a thread

# t2 = Thread(target=vai_demorar, args=('olá 2', 2))
# t2.start() # Começar a thread

# t3 = Thread(target=vai_demorar, args=('olá 3', 3))
# t3.start() # Começar a thread


# for i in range(20):
#     print(i)
#     sleep(0.5)


# Outro metódo para executar threads
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('olá 1', 10))
# t1.start()

# while t1.is_alive():
#     print('Esperando a Thread')
#     sleep(2)

# print('Thead acabou')

# Exemplo de threads
class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock() # Váriavel trava criado

    def comprar(self, quantidade):
        self.lock.acquire() # Ativa a trava para um dado por vez ser passado
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.lock.release() # Desativa a trava para outro laço entrar
            return 
        
        sleep(.5) # Dormir por 0.5 segundos
        
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso. Ainda temos {self.estoque}')

        self.lock.release() # Desativa a trava para outro laço entrar

if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        # ingressos.comprar(i)
        t = Thread(target=ingressos.comprar, args=(i,)) # criar instância da thread
        t.start() # Começar a thread

 
    print(ingressos.estoque)
