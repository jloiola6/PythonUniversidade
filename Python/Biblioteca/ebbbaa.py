try:
    from tkinter import *
except:
    from Tkinter import *

import sqlite3
from tkinter import messagebox as mb
from datetime import datetime
now = datetime.now()


counter = 0
dados = senha = author = None

def autentificador_de_email(x):
    resultado = False
    if len(x) > 9:
        if ' ' in x:
            pass
        else:
            a = x.split('@')
            if len(a) != 2 or len(a[0]) == 0:
                pass
            else:
                b = a[1].split('.')
                if len(b) != 2 and len(b) != 3 or len(b[0]) == 0:
                    pass
                elif len(b[1]) == 0:
                    pass
                else:
                    resultado = True
    return resultado

def autentificador_de_cpf(cpf):
    resultado = False
    if len(cpf) != 11 or cpf[0] == cpf[1] and cpf[1] == cpf[2] and cpf[2] == cpf[3] and cpf[3] == cpf[4] and cpf[4] == cpf[5] and cpf[5] == cpf[
        6] and cpf[6] == cpf[7] and cpf[7] == cpf[8] and cpf[8] == cpf[9] and cpf[9] == cpf[10] and cpf[10] == cpf[10]:
        return resultado
    else:
        contador = 10
        numeroj = 0
        numerok = 0
        # Descobrindo o Digito 10
        for i in (cpf)[0:9]:
            i = int(i)
            numeroj = numeroj + i * contador
            contador = contador - 1
        numeroj = numeroj % 11
        if numeroj == 0 or numeroj == 1:
            numeroj = 0
        else:
            numeroj = 11 - numeroj

        # Descobrindo o Digito 11
        contador = 11
        for i in cpf[0:10]:
            i = int(i)
            numerok = numerok + i * contador
            contador = contador - 1
        numerok = numerok % 11
        if numerok == 0 or numerok == 1:
            numerok = 0
        else:
            numerok = 11 - numerok

        # Resultado final do processo
        numeroj = str(numeroj)
        numerok = str(numerok)
        if cpf[9] == numeroj and cpf[10] == numerok:
            resultado = True
        return resultado

def ValidaData(dia, mes):
    if dia > 0 and dia <= 31:
        if mes > 0 and mes <= 12:
            return True
        else:
            return False
    else:
        return False

def cadatro():
    teste = False
    nome1 = name.get()
    if nome1 == '' or nome1.isdigit() == True:
        lname['text'] = 'Nome Inválido:*'
        lname['fg'] = 'red'
    else:
        lname['text'] = 'Nome:*'
        lname['fg'] = 'black'
    rua1 = street.get()
    if rua1 == '':
        lstreet['text'] = 'Rua Inválida:*'
        lstreet['fg'] = 'red'
    else:
        lstreet['text'] = 'Rua:*'
        lstreet['fg'] = 'black'
    bairro1 = district.get()
    if bairro1 == '':
        ldistrict['text'] = 'Bairro Inválido:*'
        ldistrict['fg'] = 'red'
    else:
        ldistrict['text'] = 'Bairro:*'
        ldistrict['fg'] = 'black'
    cidade1 = city.get()
    if cidade1 == '':
        lcity['text'] = 'Cidade Inválida:*'
        lcity['fg'] = 'red'
    else:
        lcity['text'] = 'Cidade:*'
        lcity['fg'] = 'black'
    estado1 = state.get()
    if estado1 == '':
        lstate['text'] = 'Estado Inválido:*'
        lstate['fg'] = 'red'
    else:
        lstate['text'] = 'Estado:*'
        lstate['fg'] = 'black'
    cpf = cpf1.get()
    if autentificador_de_cpf(cpf) == False:
        lcpf['text'] = 'CPF Inválido:*'
        lcpf['fg'] = 'red'
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute(f'''SELECT * FROM cliente WHERE cpf = "{cpf1.get()}"''')
        fatch = c.fetchone()
        if fatch is None:
            pass
        else:
            mb.showwarning('Aviso', 'CPF já cadastrado no banco de dados')
            teste = True
    else:
        lcpf['text'] = 'CPF:*'
        lcpf['fg'] = 'black'
    data_nascimento = date.get()
    try:
        if '/' in data_nascimento:
            dia = int(data_nascimento[:2])
            mes = int(data_nascimento[3:5])
            if ValidaData(dia, mes) == False or len(data_nascimento) != 10:
                ldate['text'] = 'Data de nascimento Inválida:*'
                ldate['fg'] = 'red'
            else:
                ldate['text'] = 'Data de Nascimento:*'
                ldate['fg'] = 'black'
        else:
            dia = int(data_nascimento[:2])
            mes = int(data_nascimento[2:4])
            if ValidaData(dia, mes) == False or len(data_nascimento) != 8:
                ldate['text'] = 'Data de nascimento Inválida:*'
                ldate['fg'] = 'red'
            else:
                ldate['text'] = 'Data de Nascimento:*'
                ldate['fg'] = 'black'
                date.insert(2, '/')
                date.insert(5, '/')
    except ValueError:
        ldate['text'] = 'Data de nascimento Inválida:*'
        ldate['fg'] = 'red'

    tel1 = tellphone.get()
    if tel1 != '':
        if tel1.isdigit() == False or len(tel1) > 10 or len(tel1) < 8:
            ltellphone['text'] = 'Telefone Residencial Inválido:'
            ltellphone['fg'] = 'red'
        else:
            ltellphone['text'] = 'Telefone Residencial:'
            ltellphone['fg'] = 'black'
    else:
        pass
    cel1 = cellphone.get()
    if cel1.isdigit() == False or len(cel1) > 11 or len(cel1) < 9:
        lcellphone['text'] = 'Celular Inválido:*'
        lcellphone['fg'] = 'red'
    else:
        lcellphone['text'] = 'Celular:*'
        lcellphone['fg'] = 'black'
    x = email.get()
    if autentificador_de_email(x) == False:
        lemail['text'] = 'Email Inválido:*'
        lemail['fg'] = 'red'
    else:
        lemail['text'] = 'Email:*'
        lemail['fg'] = 'black'
    num1 = number_of_home.get()
    if num1.isdigit() == False:
        lnumber_of_home['text'] = 'Número Inválido:*'
        lnumber_of_home['fg'] = 'red'
    else:
        lnumber_of_home['text'] = 'Número:*'
        lnumber_of_home['fg'] = 'black'

    if lstreet['fg'] == 'red' or ldistrict['fg'] == 'red' or lcity['fg'] == 'red' or lstate['fg'] == 'red' or lname[
        'fg'] == 'red' or lcpf['fg'] == 'red' or ldate['fg'] == 'red' or ltellphone['fg'] == 'red' or lcellphone['fg'] == 'red' or \
            lemail['fg'] == 'red' or lnumber_of_home['fg'] == 'red':
        if teste == False:
            mb.showerror('Erro!', 'Não foi possível salvar os dados.')
    else:
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute(f'''SELECT * FROM cliente WHERE cpf = "{cpf1.get()}"''')
        fatch = c.fetchone()
        if fatch is None:
            global date1
            date1 = date.get()
            save()
        else:
           mb.showwarning('Aviso', 'CPF já cadastrado no banco de dados')

def verification():
    global counter
    if testlogin == 'login':
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from Usuario')
        test = False
        global logined, passworded
        logined = loginedit.get()
        passworded = passwordedit.get()
        for x in c.fetchall():
            if logined == x[1] or passworded == x[2]:
                if logined == x[1] and passworded == x[2]:
                    active()
                    test = True
                    break
        if test == False:
            counter += 1
            if counter != 3:
                mb.showerror('Aviso', 'Usuário ou senha inválida')
            else:
                mb.showinfo('Aviso', 'O progama esta sendo finalizado')
                window.destroy()
    else:
        c1 = 0
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from Usuario')
        test = False
        for x in c.fetchall():
            c1 += 1
            if user.get() or password.get() in x:
                if user.get() == x[1] and password.get() == x[2]:
                    menu()
                    test = True
                    break
        if test == False:
            counter += 1
            if counter != 3:
                mb.showerror('Aviso', 'Usuário ou senha inválida')
            else:
                mb.showinfo('Aviso', 'O progama esta sendo finalizado')
                window.destroy()


        connection.commit()
        connection.close()

def actualization():
    if test_actualization == 'client':
        v2 = [cpf1, name, sex, tellphone, cellphone, email, street, district, city, state, number_of_home, date]
        tabel = ['CPF', 'nome', 'sexo', 'telefone', 'celular', 'email', 'rua', 'bairro', 'cidade', 'estado', 'numero_casa','data_de_nascimento']
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from Cliente')
        data = []
        for x in c.fetchall():
            if savecpf in x:
                data.append(x[1])
                data.append(x[2])
                data.append(x[3])
                data.append(x[4])
                data.append(x[5])
                data.append(x[6])
                data.append(x[7])
                data.append(x[8])
                data.append(x[9])
                data.append(x[10])
                data.append(x[11])
                data.append(x[12])
        for y in range(12):
            if len(v2[y].get()) != 0:
                if y != 12:
                    c.execute(f'''UPDATE Cliente
                    SET {tabel[y]} = "{v2[y].get()}"
                    WHERE CPF = "{savecpf}"''')
        connection.commit()
        connection.close()
        mb.showinfo('INFO', 'Dados Atualizados com Sucesso')
        clientwindow.destroy()

    elif test_actualization == 'author':
        conexao = sqlite3.connect('data.db')
        c = conexao.cursor()
        c.execute(f'''UPDATE Autor
                    SET nome = "{author.get()}"
                    WHERE id = "{idreference}"
                ''')
        conexao.commit()
        conexao.close()
        mb.showinfo('INFO', 'Dados Atualizados com Sucesso')

        authorwindow.destroy()


    elif test_actualization == 'book':
        conexao = sqlite3.connect('data.db')
        c = conexao.cursor()

        c.execute(f'''UPDATE Livro
            SET titulo= "{title.get()}",
            n_paginas = "{number_of_page.get()}"
            WHERE id = "{idreference}"
            ''')
        conexao.commit()
        conexao.close()

        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        valor2 = listbox2.get(0, END)
        for i in valor2:
            c.execute(f'select * from autor where nome = "{i}"')
            x = c.fetchone()
            if x[0] in dl2:
                pass
            else:
                dl2.append(x[0])
        c.execute('select * from Livro')
        valor = []
        for i in c:
            if title.get() in i[1]:
                valor = i[0]
        c.execute(f'DELETE  FROM Livro_Autor where livro = "{valor}"')
        for i in range(len(dl2)):
            c.execute(f'insert into Livro_Autor(livro, autor) values("{valor}", "{dl2[i]}");')
        connection.commit()
        connection.close()
        mb.showinfo('Aviso', 'Dados salvos com sucesso')

    elif test_actualization == 'user':
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute(f'''UPDATE Usuario
            SET Senha= "{senha.get()}"
            WHERE id = "{idreference}"
            ''')
        connection.commit()
        connection.close()
        mb.showinfo('INFO', 'Dados Atualizados com Sucesso')
        userwindow.destroy()

def active():
    if testactivate == 'client':

        var = [CheckVar1, CheckVar2, CheckVar3, CheckVar4, CheckVar5, CheckVar6, CheckVar7, CheckVar8, CheckVar9,
               CheckVar10, CheckVar11, CheckVar12]
        var2 = [cpf1, name, sex, tellphone, cellphone, email, street, district, city, state, number_of_home, date]
        for y in range(len(var)):
            if var[y].get() == 1:
                    var2[y].insert(END, d[y+1])
            elif var[y].get() == 0:
                if var2[y].get() == sex.get():
                    pass
                else:
                    var2[y].insert(END, d[y + 1])
                    var2[y].configure(state='readonly')
                    if y == 11:
                        searchwindow.destroy()
                        break
            elif y == 11:
                searchwindow.destroy()
                break
    elif testactivate == 'user':
        global idreference
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from Usuario')
        for i in c:
            for x in i:
                if logined == x:
                    login.insert(END, x)
                    login.configure(state='readonly')

        searchwindow.destroy()

    elif testactivate == 'author':
        global authorwindow, test_actualization, authorsave
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from Autor')
        authorsave = authored.get()
        for i in c.fetchall():
            if authorsave in i:
                author.insert(END, i[1])
                x = Button(authorwindow, text='Atualizar', command=actualization)
                x.place(x=10, y=300, width=100, height=25)
                idreference = i[0]
                test_actualization = 'author'
                searchwindow.destroy()

    elif testactivate == 'book':
        global bookrwindow, booksave
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from Livro')
        booksave = booked.get()
        for i in c.fetchall():
            if booksave in i:
                title.insert(END, i[1])
                title.configure('readonly')
                number_of_page.insert(END, i[2])
                x = Button(bookwindow, text='Atualizar', command=actualization)
                x.place(x=102, y=350, width=100, height=25)
                idreference = i[0]
                test_actualization = 'book'
                searchwindow.destroy()

def search_up():
    global i, testactivate
    if search_update == 'client':
        x = Button(clientwindow, text='Editar', command=actualization)
        x.place(x=325, y=300, width=100, height=25)
        global cpfed, CheckVar1, CheckVar2, CheckVar3, CheckVar4, CheckVar5, CheckVar6, CheckVar7, CheckVar8, CheckVar9, CheckVar10, CheckVar11, CheckVar12, savecpf, test_actualization, d
        testactivate = 'client'
        test_actualization = 'client'
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from cliente')
        searchwindow.geometry('450x500')
        check1 = Frame(searchwindow, width= 450, height= 60, )
        check1.place(x=0, y=250)
        check2 = Frame(searchwindow, width=450, height=60)
        check2.place(x=0, y=310)
        check3 = Frame(searchwindow, width=450, height=60)
        check3.place(x=0, y=370)
        listbox = Listbox(searchwindow, width= 68, height= 14)
        listbox.place(x= 20, y= 20)
        x = 1
        listbox.insert(END, '         DADOS DO CLIENTE')
        d = []
        for i in c:
            if cpfed.get() in i:
                winsearch.destroy()
                listbox.insert(END, f'          ID:   {i[0]}')
                listbox.insert(END, f'         CPF:   {i[1]}')
                listbox.insert(END, f'         Nome:   {i[2]}')
                listbox.insert(END, f'         Sexo:   {i[3]}')
                listbox.insert(END, f'         Telefone:   {i[4]}')
                listbox.insert(END, f'         Celular:   {i[5]}')
                listbox.insert(END, f'         Email:   {i[6]}')
                listbox.insert(END, f'         Rua:   {i[7]}')
                listbox.insert(END, f'         Bairro:   {i[8]}')
                listbox.insert(END, f'         Cidade:   {i[9]}')
                listbox.insert(END, f'         Estado:   {i[10]}')
                listbox.insert(END, f'         Numero da Casa:   {i[11]}')
                listbox.insert(END, f'         Data de Nascimento:   {i[12]}')
                savecpf = i[1]
                d.append(i[0])
                d.append(i[1])
                d.append(i[2])
                d.append(i[3])
                d.append(i[4])
                d.append(i[5])
                d.append(i[6])
                d.append(i[7])
                d.append(i[8])
                d.append(i[9])
                d.append(i[10])
                d.append(i[11])
                d.append(i[12])

                CheckVar1 = IntVar()
                CheckVar2 = IntVar()
                CheckVar3 = IntVar()
                CheckVar4 = IntVar()
                CheckVar5 = IntVar()
                CheckVar6 = IntVar()
                CheckVar7 = IntVar()
                CheckVar8 = IntVar()
                CheckVar9 = IntVar()
                CheckVar10 = IntVar()
                CheckVar11 = IntVar()
                CheckVar12 = IntVar()

                C1 = Checkbutton(check1, text="Cpf", variable=CheckVar1, onvalue=1, offvalue=0, height=1,width=10)
                C2 = Checkbutton(check1, text="Nome", variable=CheckVar2, onvalue=1, offvalue=0, height=1,width=10)
                C3 = Checkbutton(check1, text="Sexo", variable=CheckVar3, onvalue=1, offvalue=0, height=1,width=10)
                C4 = Checkbutton(check1, text="Telefone", variable=CheckVar4, onvalue=1, offvalue=0, height=1,width=10)
                C5 = Checkbutton(check2, text="Celular", variable=CheckVar5, onvalue=1, offvalue=0, height=1,width=10)
                C6 = Checkbutton(check2, text="Email", variable=CheckVar6, onvalue=1, offvalue=0, height=1,width=10)
                C7 = Checkbutton(check2, text="Rua", variable=CheckVar7, onvalue=1, offvalue=0, height=1,width=10)
                C8 = Checkbutton(check2, text="Bairro", variable=CheckVar8, onvalue=1, offvalue=0, height=1,width=10)
                C9 = Checkbutton(check3, text="Cidade", variable=CheckVar9, onvalue=1, offvalue=0, height=1,width=10)
                C10 = Checkbutton(check3, text="Estado", variable=CheckVar10, onvalue=1, offvalue=0, height=1,width=10)
                C11 = Checkbutton(check3, text="Numero  ", variable=CheckVar11, onvalue=1, offvalue=0, height=1,width=10)
                C12 = Checkbutton(check3, text="Data ", variable=CheckVar12, onvalue=1, offvalue=0, height=1, width=10)

                C1.pack(side= LEFT)
                C2.pack(side= LEFT)
                C3.pack(side= LEFT)
                C4.pack(side= LEFT)
                C5.pack(side= LEFT)
                C6.pack(side= LEFT)
                C7.pack(side= LEFT)
                C8.pack(side= LEFT)
                C9.pack(side= LEFT)
                C10.pack(side= LEFT)
                C11.pack(side= LEFT)
                C12.pack(side= LEFT)
                break

        xs = Button(searchwindow, text='Atualizar', command= active)
        xs.place(x=75, y=450, width=100, height=25)
        x = Button(searchwindow, text='Cancelar', command=searchwindow.destroy)
        x.place(x=250, y=450, width=100, height=25)

    elif search_update == 'login':
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select login from Usuario')
        for i in c.fetchall():
            if usered.get() in i:
                global loginedit, passwordedit, reference, testlogin
                winsearch.destroy()
                searchwindow.title('Verficação')
                searchwindow.geometry('350x350')

                x1 = Label(searchwindow, text='Login: ')
                x1.place(x=20, y=30)
                loginedit = Entry(searchwindow, width=50)
                loginedit.place(x=20, y=50)

                x1 = Label(searchwindow, text='Senha: ')
                x1.place(x=20, y=70)
                passwordedit = Entry(searchwindow, width=50, show= '*')
                passwordedit.place(x=20, y=90)
                reference = passwordedit.get()
                testlogin = 'login'
                test_actualization = 'user'
                testactivate = 'user'

                x = Button(searchwindow, text='Verificar', command=verification)
                x.place(x=130, y=300, width=100, height=25)
                break

def showbooks():
    try:
        listbox1.delete(0, END)
        connection = sqlite3.connect('data.db')
        c = connection.cursor()

        c.execute(f'select id from cliente where cpf = "{cpf.get()}"')
        for i in c.fetchall():
            x = i[0]

        global idbook, namebook
        teste = []
        c.execute(f'select * from cliente_livro where cliente = {x}')
        for i in c.fetchall():
            if 'Reservado' in i:
                teste.append(i)
        idbook = []
        for i in teste:
            idbook.append(i[2])
        if len(idbook) == 0:
            listbox1.insert(END, '                           ~NENHUM LIVRO CADASTRADO~')
        else:
            listbox1.delete(0, END)
            namebook = []
            for i in idbook:
                c.execute(f'select titulo from Livro where id = "{i}"')
                for i in c:
                    for x in i:
                        namebook.append(x)
            for i in namebook:
                listbox1.insert(END, i)
            global test_save
            test_save = 'perform_return'
            if test_b == True:
                x = Button(bookwindow, text='Atualizar', command=save)
                x.place(x=85, y=350, width=100, height=25)
    except:
        mb.showerror('Aviso', 'Cliente Não Encontrado')


def search():
    global search_update, winsearch,searchwindow,reference,testsearch, listbox1
    if testsearch == 'client':
        searchwindow = Toplevel()
        searchwindow.title('Pesquisa')
        searchwindow.geometry('350x350')
        winsearch = Frame(searchwindow, width=350, height=350)
        winsearch.place(x=0, y=0)
        global cpfed

        x1 = Label(winsearch, text='CPF: ')
        x1.place(x=20, y=30)
        cpfed = Entry(winsearch, width=50)
        cpfed.place(x=20, y=50)
        search_update = 'client'

        b = Button(winsearch, text='Pesquisar', command= search_up)
        b.place(x=130, y=300, width=100, height=25)

    elif testsearch == 'user':
        searchwindow = Toplevel()
        searchwindow.title('Pesquisa')
        searchwindow.geometry('350x350')
        winsearch = Frame(searchwindow, width=350, height=350)
        winsearch.place(x=0, y=0)
        global usered

        x1 = Label(winsearch, text='Usuário: ')
        x1.place(x=20, y=30)
        usered = Entry(winsearch, width=50)
        usered.place(x=20, y=50)
        search_update = 'login'

        b = Button(winsearch, text='Pesquisar', command= search_up)
        b.place(x=130, y=300, width=100, height=25)

    elif testsearch == 'author':
        searchwindow = Toplevel()
        searchwindow.title('Pesquisa')
        searchwindow.geometry('350x350')
        winsearch = Frame(searchwindow, width=350, height=350)
        winsearch.place(x=0, y=0)
        global testactivate, authored

        x1 = Label(winsearch, text='Autor: ')
        x1.place(x=20, y=30)
        authored = Entry(winsearch, width=50)
        authored.place(x=20, y=50)
        search_update = 'author'
        testactivate = 'author'

        b = Button(winsearch, text='Pesquisar', command=active)
        b.place(x=130, y=300, width=100, height=25)

    elif testsearch == 'book':
        searchwindow = Toplevel()
        searchwindow.title('Pesquisa')
        searchwindow.geometry('350x350')
        winsearch = Frame(searchwindow, width=350, height=350)
        winsearch.place(x=0, y=0)
        global booked, test_update

        x1 = Label(winsearch, text='Livro: ')
        x1.place(x=20, y=30)
        booked = Entry(winsearch, width=50)
        booked.place(x=20, y=50)
        search_update = 'book'
        testactivate = 'book'
        test_update = 'update'

        b = Button(winsearch, text='Pesquisar', command=active)
        b.place(x=130, y=300, width=100, height=25)

    elif testsearch == 'make_a_loan':
        frame.destroy()
        global bookwindow, cpf, test_b
        bookwindow.title('Cadastro de Livros')
        bookwindow.geometry('750x400')
        test_b = False

        x = Label(bookwindow, text='CPF:')
        x.place(x=25, y=40)
        cpf = Entry(bookwindow, width=30)
        cpf.place(x=25, y=60)

        x = Label(bookwindow, text='Lista de Livros Disponíveis:')
        x.place(x=500, y=80)
        test_update = ''

        frame_cadlivro1 = Frame(bookwindow)
        frame_cadlivro1.place(x=400, y=120, width=325, height=200)

        listbox2 = Listbox(frame_cadlivro1)
        listbox2.pack(fill=BOTH, expand=1)

        frame_cadlivro = Frame(bookwindow)
        frame_cadlivro.place(x=25, y=120, width=325, height=200)

        listbox1 = Listbox(frame_cadlivro)
        listbox1.pack(fill=BOTH, expand=1)
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        datasid = []
        dataidbook = []
        c.execute('select * from Cliente_Livro where devolvido = "Reservado"')
        for i in c.fetchall():
            datasid.append(i[2])
        c.execute('SELECT * FROM livro ')
        for i in c.fetchall():
            dataidbook.append(i[0])
        c.execute('SELECT * FROM livro ')
        for i in datasid:
            for v in dataidbook:
                if v == i:
                    dataidbook.remove(v)
        dataname = []
        for i in dataidbook:
            c.execute(f'select titulo from livro where id = "{i}"')
            for y in c:
                dataname.append(y[0])
        for i in dataname:
            listbox2.insert(END,f'Livro: {i}')

        x = Button(bookwindow, text='Pesquisar', command=showbooks)
        x.place(x=262, y=350, width=100, height=25)

        x = Button(bookwindow, text='Cancelar', command=bookwindow.destroy)
        x.place(x=402, y=350, width=90, height=25)


def save():
    if test_save == 'register':
        global bookwindow
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from usuario')
        test = True
        for i in c.fetchall():
            if login.get() in i:
                test = False
        if test == True:
            c.execute(f'insert into usuario (login, senha) values("{login.get()}","{senha.get()}");')
            connection.commit()
            connection.close()
            userwindow.destroy()
            mb.showinfo('Aviso', 'Dados salvos com sucesso')
        else:
            mb.showinfo('Aviso', 'Login já cadastrado')

    elif test_save == 'book':
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        valor2 = listbox2.get(0, END)
        if title.get() == '' or len(valor2) == 0 or number_of_page == '':
            mb.showerror('Aviso', 'Insira todos os dados pedidos no campo')
        else:
            if test_update == 'update':
                c.execute(f'UPDATE livro SET n_paginas = "{number_of_page.get()}" WHERE titulo = "{title.get()}"')
            else:
                c.execute(
                    'insert into livro(titulo, n_paginas) values("%s", "%s");' % (title.get(), number_of_page.get()))
            connection.commit()
            connection.close()
            connection = sqlite3.connect('data.db')
            c = connection.cursor()
            valor2 = listbox2.get(0, END)
            for i in valor2:
                c.execute(f'select * from autor where nome = "{i}"')
                x = c.fetchone()
                if x[0] in dl2:
                    pass
                else:
                    dl2.append(x[0])
            c.execute('select * from Livro')
            valor = []
            for i in c:
                valor.append(i)
            for i in range(len(valor)):
                if i == len(valor) - 1:
                    valor = valor[i]
            for i in range(len(dl2)):
                c.execute(f'insert into Livro_Autor(livro, autor) values("{valor[0]}", "{dl2[i]}");')
            connection.commit()
            connection.close()
            bookwindow.destroy()
            mb.showinfo('Aviso', 'Dados salvos com sucesso')

    elif test_save == 'client':
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('insert into cliente(cpf, nome, sexo, telefone, celular, email, rua, bairro, cidade, estado, numero_casa, data_de_nascimento) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(cpf1.get(), name.get(), sex.get(),
            tellphone.get(), cellphone.get(), email.get(), street.get(), district.get(), city.get(), state.get(), number_of_home.get(), date1))
        connection.commit()
        connection.close()
        mb.showinfo('Aviso', 'Dados salvos com sucesso')
        clientwindow.destroy()
    elif test_save == 'author':
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        c.execute('select * from autor')
        test = True
        for i in c.fetchall():
            if author.get() in i:
                test = False
        if test == True:
            c.execute('insert into autor(nome) values("%s");' % (author.get()))
            connection.commit()
            connection.close()
            authorwindow.destroy()
            mb.showinfo('Aviso', 'Dados salvos com sucesso')
        else:
            mb.showerror('Aviso', 'Autor já cadastrado')

    elif test_save == 'make_a_loan':
        teste = True
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        test_cpf = False
        cpftest = []
        c.execute('select * from cliente')
        for i in c.fetchall():
            cpftest.append(i[1])
        if cpf.get() in cpftest:
            c.execute('select * from cliente')
            dcpf = None
            for i in c.fetchall():
                if cpf.get() in i:
                    dcpf = i[0]
            c.execute('select * from livro')
            dtitle = None
            for i in c.fetchall():
                if title.get() in i:
                    dtitle = i[0]

            c.execute(f'select devolvido from Cliente_Livro where cliente = "{cpf.get()}"')
            datas = []
            x = 0
            test = True
            for i in c.fetchall():
                if 'Reservado' in i:
                    x += 1
                if x >= 5:
                    mb.showinfo('Aviso', 'Voce Ja Reservou 5 Livros')
                    test = False
                    break
            if test == True:
                x = 0
                c.execute('select * from livro')
                for i in c:
                    if title.get() in i:
                        id_author = i[0]
                    x += 1
                if x == 0:
                    x = now.ctime()
                    c.execute(
                        f'''insert into Cliente_livro(cliente, livro, data_hora_emprestimo, data_hora_devolucao, devolvido) 
                        values ("{dcpf}","{dtitle}","{x}", " ", "Reservado")''')
                    connection.commit()
                    connection.close()
                    mb.showinfo('Aviso', 'Dados salvos com sucesso')
                else:
                    c.execute('select * from Cliente_Livro')
                    datas = []
                    for i in c.fetchall():
                        for y in i:
                            datas.append(y)
                        if dtitle == datas[2] and datas[5] == 'Reservado':
                            mb.showerror('Aviso', 'Livro Esta Reservado')
                            teste = False
                            break
                        datas = []
                    if teste == True:
                        c.execute('select * from cliente')
                        dcpf = None
                        for i in c.fetchall():
                            if cpf.get() in i:
                                dcpf = i[0]
                        c.execute('select * from livro')
                        dtitle = None
                        for i in c.fetchall():
                            if title.get() in i:
                                dtitle = i[0]
                        x = now.ctime()
                        c.execute(f'''insert into Cliente_livro(cliente, livro, data_hora_emprestimo, devolvido) 
                            values("{dcpf}", "{dtitle}", "{x}", "Reservado")''')
                        connection.commit()
                        connection.close()
                        mb.showinfo('Aviso', 'Dados salvos com sucesso')
        else:
            mb.showinfo('Aviso', 'CPF não encontrado')

    elif test_save == 'perform_return':
        connection = sqlite3.connect('data.db')
        c = connection.cursor()
        valor2 = listbox2.get(0, END)
        idbook = []
        for i in valor2:
            c.execute(f'select id from livro where titulo = "{i}"')
            for x in c.fetchall():
                idbook.append(x[0])

        c.execute(f'select MAX(id) from cliente_livro where livro = "{idbook[0]}"')
        date = now.ctime()
        for i in c:
            for x in i:
                y = x
        c.execute(f'''UPDATE Cliente_Livro SET devolvido = "Disponivel", data_hora_devolucao = "{date}" where id = "{y}"''')

        connection.commit()
        connection.close()
        mb.showinfo('Aviso', 'Devoluçõe(s) efetuada(s) com sucesso!')
        bookwindow.destroy()

#                   --------------------Banco de dados--------------------
def database():
    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Cliente( 
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cpf TEXT NOT NULL,
    nome TEXT NOT NULL,
    sexo TEXT NOT NULL,
    telefone TEXT,
    celular TEXT NOT NULL,
    email TEXT NOT NULL,
    rua TEXT NOT NULL,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    numero_casa INTEGER NOT NULL,
    data_de_nascimento DATE NOT NULL
    );
    ''')
    c.execute('''CREATE TABLE IF NOT EXISTS Usuario(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    senha TEXT NOT NULL
    );
    ''')
    c.execute('''CREATE TABLE IF NOT EXISTS Autor(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    );
    ''')
    c.execute('''CREATE TABLE IF NOT EXISTS Livro(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    n_paginas TEXT NOT NULL
    );
    ''')
    c.execute('''CREATE TABLE IF NOT EXISTS Livro_Autor(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    livro INTEGER FK,
    autor INTEGER FK
    );
    ''')
    c.execute('''CREATE TABLE IF NOT EXISTS Cliente_Livro(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cliente INTEGER FK,
    livro INTEGER FK,
    data_hora_emprestimo DATETIME NOT NULL,
    data_hora_devolucao DATATIME,
    devolvido INTEGER NOT NULL
    );
    ''')
    Datalist = c.fetchall()
    connection.commit()
    connection.close()


def b_rem():
    try:
        listbox1.insert(END, listbox2.get(listbox2.curselection()))
        listbox2.delete(listbox2.curselection())
    except:
        mb.showerror('Aviso', 'Nenhum Autor Selecionado')

def b_add():
    try:
        listbox2.insert(END, listbox1.get(listbox1.curselection()))
        listbox1.delete(listbox1.curselection())
    except:
        mb.showerror('Aviso', 'Nenhum Autor Selecionado')

#                   --------------------Registro--------------------
def register_user():
    global login, senha, test_save, testsearch, userwindow
    userwindow = Toplevel()
    userwindow.title('Cadastro de Usuário')
    userwindow.geometry('350x350')

    x = Label(userwindow, text='Login: ')
    x.place(x=20, y=30)
    login = Entry(userwindow, width=50)
    login.place(x=20, y=50)

    x = Label(userwindow, text='Senha:')
    x.place(x=20, y= 70)
    senha = Entry(userwindow, width=50, show= '*')
    senha.place(x=20, y=90)

    test_save = 'register'
    testsearch = 'user'
    x = Button(userwindow, text='Pesquisar', command= search)
    x.place(x= 130, y=300, width=100, height=25)

    x = Button(userwindow, text= 'Salvar', command= save)
    x.place(x= 10, y= 300, width= 100, height= 25)

    x = Button(userwindow, text='Cancelar', command= userwindow.destroy)
    x.place(x=250, y=300, width=90, height=25)

def register_book():
    global test_save, title, number_of_page, testsearch, bookwindow, listbox1, listbox2, c1, dl2, test_update
    bookwindow = Toplevel()
    bookwindow.title('Cadastro de Livros')
    bookwindow.geometry('550x400')
    testsearch = 'book'
    test_update = ''
    test_save = 'book'


    x = Label(bookwindow, text= 'Titulo:')
    x.place(x=150, y=20)
    title = Entry(bookwindow, width=40)
    title.place(x=150, y=40)

    x = Label(bookwindow, text= 'Numero de Páginas')
    x.place(x=150, y=60)
    number_of_page = Entry(bookwindow, width=40)
    number_of_page.place(x=150, y=80)
    dl2 = []

    frame_cadlivro1 = Frame(bookwindow)
    frame_cadlivro1.place(x=320, y=120, width=200, height=200)

    s = Scrollbar(frame_cadlivro1)
    s.pack(side=RIGHT, fill=Y)
    listbox2 = Listbox(frame_cadlivro1, yscrollcommand=s.set)
    listbox2.pack(fill=BOTH, expand=1)
    s.config(command=listbox2.yview)

    frame_cadlivro = Frame(bookwindow)
    frame_cadlivro.place(x=25, y=120, width=200, height=200)

    s = Scrollbar(frame_cadlivro)
    s.pack(side=RIGHT, fill=Y)
    listbox1 = Listbox(frame_cadlivro, yscrollcommand=s.set)
    listbox1.pack(fill=BOTH, expand=1)
    s.config(command=listbox2.yview)

    conexao = sqlite3.connect('data.db')
    c = conexao.cursor()

    badd = Button(bookwindow, text='>>', command= b_add)
    badd.place(x=260, y=150)

    brem = Button(bookwindow, text='<<', command=b_rem)
    brem.place(x=260, y=220)
    c.execute('SELECT * FROM Autor')
    test = False
    for i in c.fetchall():
        listbox1.insert(END, i[1])

    x = Button(bookwindow, text='Pesquisar', command= search)
    x.place(x=222, y=350, width=100, height=25)

    x = Button(bookwindow, text='Salvar', command=save)
    x.place(x=102, y=350, width=100, height=25)

    x = Button(bookwindow, text='Cancelar', command=bookwindow.destroy)
    x.place(x=352, y=350, width=90, height=25)

def register_client():
    global test_save, cpf1, lcpf, name, lname , male, female, clientwindow, district, ldistrict, lname, state, lstate, lname,  testsearch, cellphone, lcellphone, street, lstreet, number_of_home, lnumber_of_home, sex, city, lcity, date, ldate,tellphone, ltellphone,tellphone, email, lemail
    clientwindow = Toplevel()
    clientwindow.title('Cadastro de Clientes')
    clientwindow.geometry('700x350')

    lcpf = Label(clientwindow, text= 'CPF:')
    lcpf.place(x=330, y=20)
    cpf1 = Entry(clientwindow, width=15)
    cpf1.place(x=330, y=40)

    lname = Label(clientwindow, text='Nome:')
    lname.place(x=20, y=20)
    name = Entry(clientwindow, width=45)
    name.place(x=20, y=40)

    x = Label(clientwindow, text='Sexo:')
    x.place(x=460, y=40)
    sex = StringVar()
    male = Radiobutton(clientwindow, text= 'Masculino', variable= sex, value= 'Masculino')
    male.place(x= 500, y=40)
    female = Radiobutton(clientwindow, text= 'Feminino', variable= sex, value= 'Feminino')
    female.place(x=590, y= 40)
    male.select()


    ltellphone = Label(clientwindow, text='Telefone:')
    ltellphone.place(x=20, y=60)
    tellphone = Entry(clientwindow, width=20)
    tellphone.place(x=20, y=80)

    lcellphone = Label(clientwindow, text='Celular:')
    lcellphone.place(x=180, y=60)
    cellphone = Entry(clientwindow, width=20)
    cellphone.place(x=180, y=80)

    lemail = Label(clientwindow, text='Email:')
    lemail.place(x=340, y=60)
    email = Entry(clientwindow, width=30)
    email.place(x=340, y=80)

    lstreet = Label(clientwindow, text='Rua:')
    lstreet.place(x=20, y=100)
    street = Entry(clientwindow, width=40)
    street.place(x=20, y=120)

    ldistrict = Label(clientwindow, text='Bairro:')
    ldistrict.place(x=290, y=100)
    district = Entry(clientwindow, width=25)
    district.place(x=290, y=120)

    lcity = Label(clientwindow, text='Cidade:')
    lcity.place(x=480, y=100)
    city = Entry(clientwindow, width=25)
    city.place(x=480, y=120)

    lstate = Label(clientwindow, text='Estado:')
    lstate.place(x=20, y=140)
    state = Entry(clientwindow, width=20)
    state.place(x=20, y=160)

    lnumber_of_home = Label(clientwindow, text='Numero da casa:')
    lnumber_of_home.place(x=180, y=140)
    number_of_home = Entry(clientwindow, width=20)
    number_of_home.place(x=180, y=160)

    ldate = Label(clientwindow, text='Data de Nascimento:')
    ldate.place(x=330, y=140)
    date = Entry(clientwindow, width=30)
    date.place(x=330, y=160)

    testsearch = 'client'
    test_save = 'client'

    x = Button(clientwindow, text='Pesquisar', command= search)
    x.place(x=450, y=300, width=100, height=25)

    x = Button(clientwindow, text='Salvar', command= cadatro)
    x.place(x=325, y=300, width=100, height=25)

    x = Button(clientwindow, text='Cancelar', command=clientwindow.destroy)
    x.place(x=575, y=300, width=100, height=25)

def register_author():
    global test_save, author, testsearch, authorwindow
    authorwindow = Toplevel()
    authorwindow.title('Autor')
    authorwindow.geometry('350x350')
    x = Label(authorwindow, text='Nome do autor: ')
    x.place(x=20, y=30)

    author = Entry(authorwindow, width=50)
    author.place(x=20, y=50)

    test_save = 'author'
    testsearch = 'author'

    x = Button(authorwindow, text='Pesquisar', command=search)
    x.place(x=130, y=300, width=100, height=25)

    x = Button(authorwindow, text='Salvar', command=save)
    x.place(x=10, y=300, width=100, height=25)

    x = Button(authorwindow, text='Cancelar', command=authorwindow.destroy)
    x.place(x=250, y=300, width=90, height=25)

#                   --------------------Listar--------------------
def list_author():
    list = Toplevel()
    list.title('Lista de Autores')
    list.geometry('450x400')

    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('select * from autor')
    s = Scrollbar(list)
    s.pack(side=RIGHT, fill= Y)
    listbox = Listbox(list, yscrollcommand=s.set)
    listbox.pack(expand= 1, fill=BOTH)
    s.config(command=listbox.yview)
    listbox.insert(END, '')
    x = 1
    for i in c:
        listbox.insert(END, f'         ----------AUTOR {x}----------')
        listbox.insert(END, f'          ID:   {i[0]}')
        listbox.insert(END, f'          AUTOR:   {i[1]}')
        x += 1

    list.mainloop()

def list_client():
    list = Toplevel()
    list.title('Lista de Clientes')
    list.geometry('450x400')

    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('select * from cliente')
    s = Scrollbar(list)
    s.pack(side=RIGHT, fill=Y)
    listbox = Listbox(list, yscrollcommand=s.set)
    listbox.pack(expand=1, fill=BOTH)
    s.config(command=listbox.yview)
    x = 1
    listbox.insert(END, '')
    for i in c:
        listbox.insert(END, f'         ----------PESSOA {x}----------')
        listbox.insert(END,f'          ID:   {i[0]}')
        listbox.insert(END, f'         CPF:   {i[1]}')
        listbox.insert(END, f'         NOME:   {i[2]}')
        listbox.insert(END, f'         SEXO:   {i[3]}')
        listbox.insert(END, f'         TELEFONE:   {i[4]}')
        listbox.insert(END, f'         CELULAR:   {i[5]}')
        listbox.insert(END, f'         EMAIL:   {i[6]}')
        listbox.insert(END, f'         RUA:   {i[7]}')
        listbox.insert(END, f'         BAIRRO:   {i[8]}')
        listbox.insert(END, f'         CIDADE:   {i[9]}')
        listbox.insert(END, f'         ESTADO:   {i[10]}')
        listbox.insert(END, f'         NUMERO DA CASA:   {i[11]}')
        listbox.insert(END, f'         DATA DE NASCIMENTO:   {i[12]}')
        listbox.insert(END, '')
        x += 1
    list.mainloop()

def list_book():
    list = Toplevel()
    list.title('Lista de Livros')
    list.geometry('450x400')

    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('select * from livro')
    s = Scrollbar(list)
    s.pack(side=RIGHT, fill=Y)
    listbox = Listbox(list, yscrollcommand=s.set)
    listbox.pack(expand=1, fill=BOTH)
    s.config(command=listbox.yview)
    x = 1
    for i in c:
        listbox.insert(END, f'         ----------Livro {x}----------')
        listbox.insert(END, f'          ID:   {i[0]}')
        listbox.insert(END, f'          TITULO:   {i[1]}')
        listbox.insert(END, f'          PÁGINAS:   {i[2]}')
        x += 1

    list.mainloop()

def list_user():
    list = Toplevel()
    list.title('Lista de Usuários')
    list.geometry('450x400')

    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('select id, login from usuario')
    s = Scrollbar(list)
    s.pack(side=RIGHT, fill=Y)
    listbox = Listbox(list, yscrollcommand=s.set)
    listbox.pack(expand=1, fill=BOTH)
    s.config(command=listbox.yview)
    x = 1
    for i in c:
        listbox.insert(END, f'         ----------USUÁRIO {x}----------')
        listbox.insert(END, f'          ID:   {i[0]}')
        listbox.insert(END, f'          LOGIN:   {i[1]}')
        x += 1

    list.mainloop()

def list_loan():
    list = Toplevel()
    list.title('Lista de Empréstimos')
    list.geometry('450x400')

    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('select * from Cliente_Livro')
    s = Scrollbar(list)
    s.pack(side=RIGHT, fill=Y)
    listbox = Listbox(list, yscrollcommand=s.set)
    listbox.pack(expand=1, fill=BOTH)
    s.config(command=listbox.yview)
    listbox.insert(END, '')
    for i in c:
        listbox.insert(END, f'          ID:     {i[0]}')
        listbox.insert(END, f'          ID do Cliente:     {i[1]}')
        listbox.insert(END, f'          ID do Livro:     {i[2]}')
        listbox.insert(END, f'          Data e Hora de empréstimo :     {i[3]}')
        listbox.insert(END, f'          Data e Hora de devolução:     {i[4]}')
        listbox.insert(END, f'          Situação:     {i[5]}')
        listbox.insert(END, '')
        listbox.insert(END, '-------------------------------------------------------------------------------------------')

    list.mainloop()

def list_returns():
    list = Toplevel()
    list.title('Lista de Empréstimos')
    list.geometry('450x400')

    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('select * from Cliente_Livro where devolvido = "Reservado"')
    s = Scrollbar(list)
    s.pack(side=RIGHT, fill=Y)
    listbox = Listbox(list, yscrollcommand=s.set)
    listbox.pack(expand=1, fill=BOTH)
    s.config(command=listbox.yview)
    listbox.insert(END, '')
    for i in c:
        listbox.insert(END, f'          ID:     {i[0]}')
        listbox.insert(END, f'          ID do Cliente:     {i[1]}')
        listbox.insert(END, f'          ID do Livro:     {i[2]}')
        listbox.insert(END, f'          Data e Hora de empréstimo :     {i[3]}')
        listbox.insert(END, f'          Data e Hora de devolução:     {i[4]}')
        listbox.insert(END, f'          Situação:     {i[5]}')
        listbox.insert(END, '')
        listbox.insert(END,
                       '-------------------------------------------------------------------------------------------')

    list.mainloop()

def list_book_on_loan():
    list = Toplevel()
    list.title('Lista de Empréstimos')
    list.geometry('450x400')

    connection = sqlite3.connect('data.db')
    c = connection.cursor()
    c.execute('select * from Cliente_Livro where devolvido = "Disponivel"')
    s = Scrollbar(list)
    s.pack(side=RIGHT, fill=Y)
    listbox = Listbox(list, yscrollcommand=s.set)
    listbox.pack(expand=1, fill=BOTH)
    s.config(command=listbox.yview)
    listbox.insert(END, '')
    for i in c:
        listbox.insert(END, f'          ID:     {i[0]}')
        listbox.insert(END, f'          ID do Cliente:     {i[1]}')
        listbox.insert(END, f'          ID do Livro:     {i[2]}')
        listbox.insert(END, f'          Data e Hora de empréstimo :     {i[3]}')
        listbox.insert(END, f'          Data e Hora de devolução:     {i[4]}')
        listbox.insert(END, f'          Situação:     {i[5]}')
        listbox.insert(END, '')
        listbox.insert(END,
                       '-------------------------------------------------------------------------------------------')

    list.mainloop()

#                   ---------------Empréstimo---------------
def make_a_loan():
    global testsearch, test_save, cpf, title, frame, bookwindow
    bookwindow = Toplevel()
    bookwindow.title('Realizar Empréstimo')
    bookwindow.geometry('350x350')
    frame = Frame(bookwindow)
    frame.pack(fill= BOTH, expand= 1)
    bookwindow.grab_set()

    x = Label(frame, text='CPF:')
    x.place(x=20, y=30)

    cpf = Entry(frame, width=50)
    cpf.place(x=20, y=50)

    x = Label(frame, text='Livro:')
    x.place(x=20, y=70)

    title = Entry(frame, width=50)
    title.place(x=20, y=90)

    test_save = 'make_a_loan'
    testsearch = 'make_a_loan'

    x = Button(frame, text='Cadastrar', command=save)
    x.place(x=15, y=300, width=100, height=25)

    x = Button(frame, text='Procurar', command=search)
    x.place(x=125, y=300, width=100, height=25)

    x = Button(frame, text='Cancelar', command=bookwindow.destroy)
    x.place(x=235, y=300, width=100, height=25)

    frame.mainloop()

def perform_return():
    global bookwindow, listbox1, cpf, listbox2, test_save, test_b
    bookwindow = Toplevel()
    bookwindow.title('Cadastro de Livros')
    bookwindow.geometry('750x400')
    bookwindow.grab_set()
    test_b =True

    x = Label(bookwindow, text='CPF:')
    x.place(x=25, y=40)
    cpf = Entry(bookwindow, width=30)
    cpf.place(x=25, y=60)

    x = Label(bookwindow, text='Lista de Livros Para Devoluções:')
    x.place(x=500, y=80)
    test_save = 'perform_return'

    frame_cadlivro1 = Frame(bookwindow)
    frame_cadlivro1.place(x=400, y=120, width=325, height=200)

    listbox2 = Listbox(frame_cadlivro1)
    listbox2.pack(fill=BOTH, expand=1)

    frame_cadlivro = Frame(bookwindow)
    frame_cadlivro.place(x=25, y=120, width=325, height=200)

    listbox1 = Listbox(frame_cadlivro)
    listbox1.pack(fill=BOTH, expand=1)

    badd = Button(bookwindow, text='>>', command=b_add)
    badd.place(x=360, y=150)

    brem = Button(bookwindow, text='<<', command=b_rem)
    brem.place(x=360, y=220)

    x = Button(bookwindow, text='Pesquisar', command=showbooks)
    x.place(x=257, y=350, width=100, height=25)

    x = Button(bookwindow, text='Cancelar', command=bookwindow.destroy)
    x.place(x=387, y=350, width=90, height=25)

#                   ---------------Menu---------------
def menu():
    windowlogin.destroy()

    menu_bar = Menu(window)
    main_menu = Menu(menu_bar, tearoff= 0)
    menu_bar.add_cascade(label= 'Cadastrar', menu= main_menu)
    main_menu.add_command(label= 'Autor', command= register_author)
    main_menu.add_command(label= 'Cliente', command= register_client)
    main_menu.add_command(label= 'Livro', command= register_book)
    main_menu.add_command(label= 'Usuário', command= register_user)

    main_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Listar', menu=main_menu)
    main_menu.add_command(label='Autores', command= list_author)
    main_menu.add_command(label='Clientes', command= list_client)
    main_menu.add_command(label='Livros', command= list_book)
    main_menu.add_command(label='Usuários', command= list_user)
    main_menu.add_command(label='Empréstimos', command= list_loan)
    main_menu.add_command(label='Devoluções', command= list_returns)
    main_menu.add_command(label='Livros Empréstados', command= list_book_on_loan)

    main_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Empréstimo', menu=main_menu)
    main_menu.add_command(label='Realizar Empréstimo', command= make_a_loan)
    main_menu.add_command(label='Realizar Devolução', command= perform_return)

    main_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Sair', menu=main_menu)
    main_menu.add_command(label='Sair', command= window.destroy)
    window.config(menu= menu_bar)

database()

window = Tk()
window.title('Menu')
window.geometry('450x350')
windowlogin = Frame(window, width= 450, height= 350)
windowlogin.place(x=0,y=0)
testlogin = 'menu'


labeluser = Label(windowlogin, text='Usuário: ')
labeluser.place(x=130, y=30)
user = Entry(windowlogin, width=30)
user.place(x=130, y=50)
user.focus_set()

labelpassword = Label(windowlogin, text='Senha: ')
labelpassword.place(x=130, y=80)
password = Entry(windowlogin, width=30, show='*')
password.place(x=130, y=100)

x1 = Button(windowlogin, text='Login', command= menu)
x1.place(x=100, y=180, width=100, height=25)

x2 = Button(windowlogin, text='Sair', command=window.destroy)
x2.place(x=250, y=180, width=100, height=25)

window.mainloop()


#                   ----------Classe de Cadastros----------
'''class Register():
    def register_user(self):
        self.userwindow = Toplevel()
        self.userwindow.title('Cadastro de Usuário')
        self.userwindow.geometry('750x500')
        self.datas = ['nome', 'cpf']
        self.b = 30
        for self.i in self.datas:
            if i != 'CPF':
                self.x = Label(self.userwindow, text= self.i.title() + ':')
            else:
                self.x = Label(self.userwindow, text= self.i + ':')
            self.x.place(x=20, y=self.b)
            self.b += 20
            self.i = Entry(self.userwindow, width=50)
            self.i.place(x=20, y=self.b)
            self.b += 20

        self.login = datas[0]
        self.senha = datas[1]
        self.c.execute('insert into cadastros(login, senha) values("%s", "%s");' % (self.login, self.senha))
        self.c.commit()

        self.userwindow.mainloop()

    def register_book(self):
        self.bookwindow = Toplevel()
        self.bookwindow.title('Cadastro de Livros')
        self.bookwindow.geometry('750x500')
        self.datas = ['titulo', 'numero de páginas']
        self.c = 30
        for self.i in self.datas:
            self.x = Label(self.bookwindow, text= self.i.title() + ':')
            self.x = Label(self.bookwindow, text= self.i + ':')
            self.x.place(x=20, y=c)
            self.c += 20
            self.i = Entry(self.bookwindow, width=50)
            self.i.place(x=20, y=self.c)
            self.c += 20
        self.bookwindow.mainloop()

    def register_client(self):
        self.clientwindow = Toplevel()
        self.clientwindow.title('Cadastro de Clientes')
        self.clientwindow.geometry('750x500')
        self.datas = ['CPF', 'nome', 'bairro', 'rua', 'numero da casa', 'bairro', 'sexo', 'data de nascimento', 'telefone',
                 'email']
        self.c = 30
        for self.i in self.datas:
            if i != 'CPF':
                self.x = Label(clientwindow, text=i.title() + ':')
            else:
                self.x = Label(clientwindow, text=i + ':')
            self.x = Label(clientwindow, text=i + ':')
            self.x.place(x=20, y=c)
            self.c += 20
            self.i = Entry(clientwindow, width=50)
            self.i.place(x=20, y=c)
            self.c += 20
        if self.geraltest == True:
            pass
        clientwindow.mainloop()

    def register_author(self):
        pass

    def __init__(self):
        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        self.b4.destroy()

        self.window.title('Cadastro')

        self.x1 = Button(window, text='Autor')
        self.x1.place(x=100, y=100, width=100, height=25)

        self.x2 = Button(window, text='Cliente', command=register_client)
        self.x2.place(x=250, y=100, width=100, height=25)

        self.x3 = Button(window, text='Livro', command=register_book)
        self.x3.place(x=100, y=200, width=100, height=25)

        self.x4 = Button(window, text='Usuário', command=register_user)
        self.x4.place(x=250, y=200, width=100, height=25)

        self.window.mainloop()

'''