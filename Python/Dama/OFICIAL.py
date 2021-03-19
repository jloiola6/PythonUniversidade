#---------------------Jogo de Dama---------------------------
try:
    from tkinter import *
    from tkinter import messagebox as mb
except:
    from Tkinter import *
    from Tkinter import messagebox as mb

class Peca(object):
    dama = False
    def __init__(self, cor, posicao):
        self.cor = cor
        self.posicao = posicao
        self.dama = False
     # def mover(self, posicao):
     #     pass
    def virar_dama(self):
        pass

class Tabuleiro(Peca):

    b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = b10 = b11 = b12 = b13 = b14 = b15 = b16 = b17 = b18 = b19 = b20 = b21 = b22 = b23 = b24 = b25 = b26 = b27 = b28 = b29 = b30 = b31 = b32 = None
    canvas = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22,
                   b23, b24, b25, b26, b27, b28, b29, b30, b31, b32]
    def __init__(self):
        self.jogador = 'branco'
        self.pecas_branca = self.pecas_preta = 12

        self.matriz = [True, Peca('Preta', (5, 1)), True, Peca('Preta', (5, 3)), True, Peca('Preta', (5, 5)), True, Peca('Preta', (5, 7))], \
                    [Peca('Preta', (6, 0)), True, Peca('Preta', (6, 2)), True, Peca('Preta', (6, 4)), True, Peca('Preta', (6, 6)), True], \
                    [True, Peca('Preta', (7, 0)), True, Peca('Preta', (7, 2)), True, Peca('Preta', (7, 4)), True, Peca('Preta', (7, 6))],\
                    [False, True, False, True, False, True, False, True], \
                    [True, False, True, False, True, False, True, False], \
                    [Peca('Branca', (0, 0)), True, Peca('Branca', (0, 2)), True, Peca('Branca', (0, 4)), True, Peca('Branca', (0, 6)), True], \
                    [True, Peca('Branca', (1, 1)), True, Peca('Branca', (1, 3)), True, Peca('Branca', (1, 4)), True, Peca('Branca', (1, 5))], \
                    [Peca('Branca', (2, 0)), True, Peca('Branca', (2, 2)), True, Peca('Branca', (2, 4)), True, Peca('Branca', (2, 6)), True]

        self.root = Tk()
        self.root.geometry('600x600')
        self.root.resizable(False, False)
        
        self.contador = 0
        self.c = 0
        self.a = 0
        self.b = 0
        for l in range(8):
            for c in range(8):
                if self.matriz[l][c] !=True:
                    self.peca = self.matriz[l][c]
                    self.canvas[self.c] = Canvas(self.root, width=70, height=70, cursor='hand2', bg='red')
                    self.canvas[self.c].place(x= self.a, y= self.b)

                    if self.peca == False:
                        pass
                    elif self.peca.cor == 'Branca':
                        pass
                        self.canvas[self.c].create_oval(15,20,60,60, fill= 'white', outline= 'black')
                    else:
                        pass
                        self.canvas[self.c].create_oval(15,20,60,60, fill= 'black', outline= 'white')
                    self.c += 1
                self.a += 75
            self.a = 0
            self.b += 75

        self.root.bind('<Button-1>', self.callback)

        self.root.mainloop()

    def callback(self, event):
        try:
            sad = str((event.widget))
            x = (sad.split('s'))[1]
            if x == '':
                x = 1
            x = int(x) - 1



            if self.contador%2 == 0:
                self.teste = True
                self.c = 0
                for l in range(8):
                    for c in range(8):
                        if self.matriz[l][c] != True:
                            if x == self.c:
                                if self.matriz[l][c] == False:
                                    self.teste = False
                                    mb.showerror('Atenção', 'Selecione uma peca para efetuar uma jogada')
                            self.c += 1

                if self.teste == True:
                    self.contador += 1
                    self.c = 0
                    for l in range(8):
                        for c in range(8):
                            if self.matriz[l][c] != True:
                                if x == self.c:
                                    self.cor = self.matriz[l][c].cor
                                    self.posicao1 = x
                                    self.matriz[l][c] = False
                                    # if self.cor == 'Branca':
                                    #     self.canvas[self.posicao1].create_oval(15, 20, 60, 60, fill='red', outline='red')
                                    # else:
                                    #     self.canvas[self.posicao1].create_oval(15, 20, 60, 60, fill='red', outline='red')
                                self.c += 1
            else:
                self.c = 0
                for l in range(8):
                    for c in range(8):
                        if self.matriz[l][c] != True:
                            if x == self.c:
                                if self.matriz[l][c] == False:
                                    self.contador += 1
                                    self.canvas[self.posicao1].create_oval(15, 20, 60, 60, fill='red', outline='red')
                                    if self.cor == 'Preta':
                                        self.canvas[x].create_oval(15, 20, 60, 60, fill='black', outline='white')
                                        self.matriz[l][c] = Peca('Preta', (l, c))
                                    else:
                                        self.canvas[x].create_oval(15, 20, 60, 60, fill='white', outline='black')
                                        self.matriz[l][c] = Peca('Branca', (l, c - 1))
                                elif self.matriz[l][c].cor == 'Branca' or self.matriz[l][c].cor == 'Preta':
                                    mb.showerror('Atenção', 'Não pode trocar uma peça pela outra')


                            self.c += 1
        except:
            print('erro')

x = Tabuleiro()