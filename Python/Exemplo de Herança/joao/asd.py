class Pessoa():
    nome = cpf = None
    def dados(self):
        for i, j in self.__dict__.items():
            # if i[0] != '_':
            print(f'{i}: {j}')

class Homem(Pessoa):
    sexo = 'Masculino'
    def jogar(self):
        print('Esporte: Joga bola')
    def hobbie(self):
        print('Passa tempo: Ver desenhos')

class Mulher(Pessoa):
    sexo = 'Feminino'
    def jogar(self):
        print('Joga volei')
    def hobbie(self):
        print('Passa tempo: Kung fu')

class Filha(Mulher, Homem):
    def mostrar(self):
        super().jogar()
        super().hobbie()

class Filho(Homem, Mulher):
    def mostrar(self):
        super().jogar()
        super().hobbie()

nome = input('Digite seu nome: ')
cpf = input('Digte seu cpf: ')
sexo = input('Digite seu Sexo: ')
print('-' * 20)

if sexo == 'M':
    f = Filho()
else:
    f = Filha()

f.nome = nome
f.cpf = cpf
# h._Homem__sexo = 'Desconhecido'
f.dados()
f.mostrar()
print(f.sexo)

#estudar sobre "Mixin"
