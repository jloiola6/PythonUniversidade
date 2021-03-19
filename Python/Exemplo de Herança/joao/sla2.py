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
        self.vez = 'Branca'

        self.matriz = [True, Peca('Preta', (5, 1)), True, Peca('Preta', (5, 3)), True, Peca('Preta', (5, 5)), True, Peca('Preta', (5, 7))], \
                      [Peca('Preta', (6, 0)), True, Peca('Preta', (6, 2)), True, Peca('Preta', (6, 4)), True, Peca('Preta', (6, 6)), True], \
                      [True, Peca('Preta', (7, 0)), True, Peca('Preta', (7, 2)), True, Peca('Preta', (7, 4)), True, Peca('Preta', (7, 6))], \
                      [False, True, False, True, False, True, False, True], \
                      [True, False, True, False, True, False, True, False], \
                      [Peca('Branca', (0, 0)), True, Peca('Branca', (0, 2)), True, Peca('Branca', (0, 4)), True, Peca('Branca', (0, 6)), True], \
                      [True, Peca('Branca', (1, 1)), True, Peca('Branca', (1, 3)), True, Peca('Branca', (1, 4)), True, Peca('Branca', (1, 5))], \
                      [Peca('Branca', (2, 0)), True, Peca('Branca', (2, 2)), True, Peca('Branca', (2, 4)), True, Peca('Branca', (2, 6)), True]


        self.root = Tk()
        self.root.geometry('595x595')
        self.root.resizable(False, False)
        self.root['bg'] = 'white'

        self.contador = 0
        self.c = 0
        self.a = 0
        self.b = 0
        self.ce2 = None
        self.cd2 = None

        for l in range(8):
            for c in range(8):
                if self.matriz[l][c] !=True:
                    self.peca = self.matriz[l][c]
                    self.canvas[self.c] = Canvas(self.root, width=75, height=75, cursor='hand2', bg='red')
                    self.canvas[self.c].place(x= self.a, y= self.b)
                    if self.peca == False:
                        pass
                    elif self.peca.cor == 'Branca':
                        self.canvas[self.c].create_oval(15,15,55,55, fill= 'white', outline= 'black')
                    else:
                        self.canvas[self.c].create_oval(15,15,55,55, fill= 'black', outline= 'white')
                    self.c += 1
                self.a += 75
            self.a = 0
            self.b += 75

        self.root.bind('<Button-1>', self.callback)

        self.root.mainloop()

    def callback(self, event):
        # try:
        sad = str((event.widget))
        x = (sad.split('s'))[1]
        if x == '':
            x = 1
        x = int(x) - 1
        if self.contador%2 == 0:
            #Detecta a peca, declara como falsa na matriz e slva suas caracteristica além de um Backup
            self.c = 0
            for l in range(8):
                for c in range(8):
                    if self.matriz[l][c] != True:
                        if x == self.c:
                            print(x)
                            self.cor = self.matriz[l][c].cor
                            self.peca = self.matriz[l][c]
                            self.posicao1 = x
                            # self.matriz[l][c] = False
                            self.escolha = (l,c)
                        self.c += 1

            if self.cor == self.vez:
                self.verificacao = False
                self.c = 0
                for l in range(8):
                    for c in range(8):
                        if self.matriz[l][c] != True:
                            if x == self.c:
                                if self.cor == 'Preta':
                                    try:
                                        if self.matriz[l + 1][c - 1] != False or self.matriz[l+1][c+1] != False:
                                            if self.matriz[l + 1][c - 1] == False or self.matriz[l + 1][c + 1] == False:
                                                self.verificacao = False
                                                print('oi')
                                                if self.matriz[l + 2][c - 2] == False or self.matriz[l+2][c+2] == False:
                                                    print('opaaaa')
                                                    self.verificacao = True
                                    except:
                                        print('erro')
                                else:
                                    try:
                                        if self.matriz[l - 1][c - 1] != False or self.matriz[l-1][c+1] != False:
                                            if self.matriz[l - 1][c - 1] == False or self.matriz[l - 1][c + 1] == False:
                                                self.verificacao = False
                                                print('oi')
                                                if self.matriz[l - 2][c - 2] == False or self.matriz[l-2][c+2] == False:
                                                    print('opaaaa')
                                                    self.verificacao = True
                                    except:
                                        pass
                            self.c += 1

                if self.verificacao == True:
                    # Determina (com bolinhas) aonde podem ser a possiveis jogadas com objetivo de COMER PEÇAS!!!!
                    self.c = 0
                    for l in range(8):
                        for c in range(8):
                            if self.matriz != True:
                                if self.cor == 'Preta':
                                    if l == (self.escolha[0] + 2):
                                        if c == (self.escolha[1] - 2):
                                            try:
                                                if self.matriz[self.escolha[0] + 2][self.escolha[1] - 2] == False:
                                                    if self.matriz[self.escolha[0] + 1][self.escolha[1] - 1].cor == 'Branca':
                                                        self.lado = 'Esquerda'
                                                        self.ce2 = x + 7
                                                        self.canvas[self.ce2].create_oval(30, 30, 45, 45, fill='black', outline='red')
                                                    else:
                                                        self.teste1 = False
                                            except:
                                                pass
                                        if c == (self.escolha[1] + 2):
                                            try:
                                                if self.matriz[self.escolha[0] + 2][self.escolha[1] + 2] == False:
                                                    if self.matriz[self.escolha[0] + 1][self.escolha[1] + 1].cor == 'Branca':
                                                        self.lado = 'Direita'
                                                        self.cd2 = x + 9
                                                        self.canvas[self.cd2].create_oval(30, 30, 45, 45, fill='black', outline='red')
                                                else:
                                                    self.teste2 = False
                                            except:
                                                pass
                                else:
                                    if l == (self.escolha[0] - 2):
                                        if c == (self.escolha[1] - 2):
                                            try:
                                                if self.matriz[self.escolha[0] - 2][self.escolha[1] - 2] == False:
                                                    if self.matriz[self.escolha[0] - 1][self.escolha[1] - 1].cor == 'Preta':
                                                        self.lado = 'Esquerda'
                                                        self.ce2 = x - 9
                                                        self.canvas[self.ce2].create_oval(30, 30, 45, 45, fill='white', outline='red')
                                                else:
                                                    self.teste1 = False
                                            except:
                                                pass
                                        if c == (self.escolha[1] - 2):
                                            try:
                                                if self.matriz[self.escolha[0] - 2][self.escolha[1] + 2] == False:
                                                    if self.matriz[self.escolha[0] - 1][self.escolha[1] + 1].cor == 'Preta':
                                                        self.lado = 'Direita'
                                                        self.cd2 = x -7
                                                        self.canvas[self.cd2].create_oval(30, 30, 45, 45, fill='white', outline='red')
                                                else:
                                                    self.teste2 = False
                                            except:
                                                pass
                                self.c += 1
                    self.ce = self.cd = None
                else:
                    #Determina (com bolinhas) aonde podem ser a possiveis jogadas SIMPLES
                    self.teste1 = self.teste2 = True
                    self.c = 0
                    for l in range(8):
                        for c in range(8):
                            if self.matriz[l][c] != True:
                                if self.cor == 'Preta':
                                    if l == (self.escolha[0]  + 1):
                                        if c == (self.escolha[1] - 1):
                                            try:
                                                if self.matriz[self.escolha[0]+1][self.escolha[1] - 1] == False:
                                                    self.ce = self.c
                                                    self.canvas[self.c].create_oval(30, 30, 45, 45, fill='black', outline='red')
                                                else:
                                                    self.teste1 = False
                                            except:
                                                pass
                                        if c == (self.escolha[1] + 1):
                                            try:
                                                if self.matriz[self.escolha[0] + 1][self.escolha[1] + 1] == False:
                                                    self.cd = self.c
                                                    self.canvas[self.c].create_oval(30, 30, 45, 45, fill='black', outline='red')
                                                else:
                                                    self.teste2 = False
                                            except:
                                                pass
                                else:
                                    if l == (self.escolha[0]  - 1):
                                        if c == (self.escolha[1] - 1):
                                            try:
                                                if self.matriz[self.escolha[0] - 1][self.escolha[1] - 1] == False:
                                                    self.ce = self.c
                                                    self.canvas[self.c].create_oval(30, 30, 45, 45, fill='white', outline='red')
                                                else:
                                                    self.teste1 = False
                                            except:
                                                pass
                                        if c == (self.escolha[1] + 1):
                                            try:
                                                if self.matriz[self.escolha[0] - 1][self.escolha[1] + 1] == False:
                                                    self.cd = self.c
                                                    self.canvas[self.c].create_oval(30, 30, 45, 45, fill='white', outline='red')
                                                else:
                                                    self.teste2 = False
                                            except:
                                                pass
                                self.c += 1


                if self.teste1 == False and self.teste2 == False:
                    self.contador -= 2
                    self.matriz[self.escolha[0]][self.escolha[1]] = self.peca
                    mb.showinfo('Aviso', 'Não pode selecionar essa peça pois não há movimento para ela')
                    # self.contador -= 1
                else:
                    self.contador += 1


            else:
                self.matriz[self.escolha[0]][self.escolha[1]] = self.peca
                mb.showwarning('Aviso', 'Não é sua vez.')

        else:
            self.c = 0
            self.move = False
            self.espaco = False
            for l in range(8):
                for c in range(8):
                    if self.matriz[l][c] != False:
                        if x == self.ce2 or x == self.cd2:
                            self.move = 'Comer'
                            self.espaco = True
                        elif x == self.ce or x == self.cd:
                            self.move = 'Simples'
                            self.espaco = True
                        self.c += 1
            if self.espaco != True:
                self.matriz[self.escolha[0]][self.escolha[1]] = self.peca
                self.contador -= 1
                mb.showerror('Aviso', 'Jogada não permitida')
                self.c = 0
                for l in range(8):
                    for c in range(8):
                        if self.matriz[l][c] != True:
                            if self.matriz[l][c] == False:
                                self.canvas[self.c].create_oval(15, 15, 55, 55, fill='red', outline='red')
                            self.c += 1

            else:
                if self.move == 'Simples':
                    self.c = 0
                    for l in range(8):
                        for c in range(8):
                            if self.matriz[l][c] != True:
                                if x == self.c:
                                    if self.matriz[l][c] == False:
                                        self.contador += 1
                                        if self.cor == 'Branca':
                                            self.vez = 'Preta'
                                        else:
                                            self.vez = 'Branca'

                                        if self.cor == 'Preta':
                                            self.canvas[x].create_oval(15, 15, 55, 55, fill='black', outline='white')
                                            self.matriz[l][c] = Peca('Preta', (l, c))
                                        else:
                                            self.canvas[x].create_oval(15, 15, 55, 55, fill='white', outline='black')
                                            self.matriz[l][c] = Peca('Branca', (l, c - 1))
                                    elif self.matriz[l][c].cor == 'Branca' or self.matriz[l][c].cor == 'Preta':
                                        mb.showerror('Atenção', 'Não pode trocar uma peça pela outra')
                                        self.matriz[self.escolha[0]][self.escolha[1]] = self.peca
                                        self.contador -= 3
                                self.c += 1
                elif self.move == 'Comer':
                    self.c = 0
                    for l in range(8):
                        for c in range(8):
                            if self.matriz[l][c] != True:
                                if x == self.c:
                                    if self.matriz[l][c] == False:
                                        self.contador += 1
                                        if self.cor == 'Preta':
                                            if self.lado == 'Direita':
                                                self.matriz[l-1][c-1] = False
                                            else:
                                                self.matriz[l-1][c+1] = False

                                            self.canvas[x].create_oval(15, 15, 55, 55, fill='black', outline='white')
                                            self.matriz[l][c] = Peca('Preta', (l, c))

                                            if self.cor == 'Branca':
                                                self.vez = 'Preta'
                                            else:
                                                self.vez = 'Branca'
                                        else:
                                            if self.lado  == 'Direita':
                                                self.matriz[l+1][c-1] = False
                                            else:
                                                self.matriz[l + 1][c + 1] = False
                                            self.canvas[x].create_oval(15, 15, 55, 55, fill='white', outline='black')
                                            self.matriz[l][c] = Peca('Branca', (l, c))

                                            if self.cor == 'Branca':
                                                self.vez = 'Preta'
                                            else:
                                                self.vez = 'Branca'

                                    elif self.matriz[l][c].cor == 'Branca' or self.matriz[l][c].cor == 'Preta':
                                        mb.showerror('Atenção', 'Não pode trocar uma peça pela outra')
                                        self.matriz[self.escolha[0]][self.escolha[1]] = self.peca
                                        self.contador -= 3
                                self.c += 1
                self.matriz[self.escolha[0]][self.escolha[1]] = False
                self.c = 0
                for l in range(8):
                    for c in range(8):
                        if self.matriz[l][c] != True:
                            if self.matriz[l][c] == False:
                                self.canvas[self.c].create_oval(15, 15, 55, 55, fill='red', outline='red')
                            self.c += 1

        # except:
        #     self.contador -= 1
        #     # self.matriz[self.escolha[0]][self.escolha[1]] = self.peca
        #     mb.showwarning('Aviso', 'Selecione um campo jogável')
        #     self.c = 0
        #     for l in range(8):
        #         for c in range(8):
        #             if self.matriz[l][c] != True:
        #                 if self.matriz[l][c] == False:
        #                     self.canvas[self.c].create_oval(15, 15, 55, 55, fill='red', outline='red')
        #                 self.c += 1

x = Tabuleiro()
