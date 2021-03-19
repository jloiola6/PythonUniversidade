from tkinter import *
from time import sleep
from threading import Thread

root = Tk()
root.title('Principal')
root.geometry('600x400+500+100')
root.resizable(False, False)


class Janela():
    def acao(self):
        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.b4.destroy()
        self.rodar = True
        print(self.rodar)

        self.labrador = Labrador()
        

    def eba(self):
        self.labrador.start()
        
    def __init__(self, root, teste):
        self.root = root
        self.teste = teste
        #Frame 
        self.framemeio = Frame(self.root, height= 400, width = 600)
        self.framemeio.place(x= 0, y=50)

        if self.teste == False:
            self.b1 = Button(self.framemeio, height= 3, width= 10, text= 'Labrador', command= self.acao)
            self.b1.place(x= 100, y= 50)

            self.b2 = Button(self.framemeio, height= 3, width= 10, text= 'Persa', command= Persa)
            self.b2.place(x= 500, y= 50)

            self.b3 = Button(self.framemeio, height= 3, width= 10, text= 'Vira Lata', command= Vira_lata)
            self.b3.place(x= 500, y= 180)

            self.b4 = Button(self.framemeio, height= 3, width= 10, text= 'Siames', command= Siames)
            self.b4.place(x= 100, y= 180)

        #Frame Baixo
        self.framebaixo = Frame(self.root, height= 100, width= 600)
        self.framebaixo.place(x= 0, y=300)

        self.botao = Button(self.framebaixo, height= 3, width= 6, text= 'Start', command='')
        self.botao.place(x= 280, y= 40)
    

class Mamifero():
    def principal(self):
        self.pelo = input('Pelo: ')
        self.olhos = input('Olhos: ')
        self.sexo = input('Sexo: ')
        self.peso = input('Peso: ')
        print('-' * 20)
   
    #def __str__(self):
        #return f'Pelo: {self.pelo}\nOlhos: {self.olhos}\nSexo: {self.sexo}\nPeso: {self.peso}\n'

class Gato():
    def atualizar(self):
        self.som = 'Miar'
        self.alimentacao = 'Rato'
        self.higienico = 'Sim'
        self.comportamento = 'Calmo'
  
    def printar(self):
        print(f'{super().principal()}Pelo: {self.pelo}\nOlhos: {self.olhos}\nSexo: {self.sexo}\nPeso: {self.peso}\nSom: {self.som}\nAlimentação: {self.alimentacao}\nComportamento: {self.comportamento}')
        
class Cachorro():
    def atualizar(self):
        self.som = 'Latir'
        self.alimentacao = 'Gato'
        self.higienico = 'Não'
        self.comportamento = 'Agitado'

    def printar(self):
        print(f'{super().principal()}Pelo: {self.pelo}\nOlhos: {self.olhos}\nSexo: {self.sexo}\nPeso: {self.peso}\nSom: {self.som}\nAlimentação: {self.alimentacao}\nComportamento: {self.comportamento}')        

class Siames(Gato, Mamifero, Janela):
    def __init__(self):
        print('Raça: Siames')
        super().__init__(root)

        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.b4.destroy()

        siames = PhotoImage(file="Siames.png")
        s = Label(self.framemeio, image=siames)
        s.image = siames
        s.place(x= 400, y= 150)

class Vira_lata(Cachorro, Mamifero, Janela):
    def __init__(self):
        print('Raça: Vira Lata')
        super().__init__(root)

        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.b4.destroy()

        vira_lata = PhotoImage(file="Vira_lata.png")
        v = Label(self.framemeio, image=vira_lata)
        v.image = vira_lata
        v.place(x= 400, y= 20)

class Labrador(Janela, Thread, Cachorro, Mamifero):
    def __init__(self):
        print('Raça: Labrador')
        super().__init__(root, True)        
        self.rodar = True
        if self.rodar == True:
            print('asdasdasd')
            super(Labrador, self).__init__(root, True)
            
            labrador = PhotoImage(file="Labrador.png")
            l = Label(self.framemeio, image=labrador)
            l.image = labrador
            self.x, self.y = 10, 20
            l.place(x= self.x, y= self.y)
    def run(self):
        print('-'*20)
        n = 10
        while True:
            self.l.place(x=self.x+n, y=self.y)
            self.l = self.x+n

class Persa(Gato, Mamifero, Janela):
    def __init__(self):
        print('Raça: Persa')
        teste = True
        super().__init__(root, teste)

        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.b4.destroy()

        persa = PhotoImage(file="Persa.png")
        p = Label(self.framemeio, image=persa)
        p.image = persa
        p.place(x= 10, y= 150)

#y = input('1- Siames\n2- Vira Lata\n3- Labrador\n4- Persa\n')
#if y == '1':
#    x = Siames()
#elif y == '2':
#    x = Vira_lata()
#elif y == '3':
#    x = Labrador()
#elif y == '4':
#    x = Persa()
#else:
#    print('opa')
x = Janela(root, False)
try:
    x.mostrar(root)
except:
    pass

root.mainloop()