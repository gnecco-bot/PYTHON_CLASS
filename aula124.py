class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando is True:
            print(f'{self.nome} Já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def para_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando is True:
            print(f'{self.nome} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando...')

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
print(f'Estado da Canon {c1.filmando}')
print(f'Estado da Sony {c2.filmando}')
c1.filmar()
c1.fotografar()
c1.para_filmar()
c1.fotografar()
print()
c2.para_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.para_filmar()
c2.fotografar()
print(f'Estado da Sony {c2.filmando}')