try:
    from tkinter import *
except:
    from Tkinter import *

import sqlite3

class Banco():
    def __init__(self):
        connection = sqlite3.connect('Data.db')
        c = connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS People(
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  Name VARCHAR,
                  Phone1 VARCHAR,
                  Phone2 VARCHAR
                  );
                  ''')
        c.execute('''CREATE TABLE IF NOT EXISTS Meeting(
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  Description VARCHAR,
                  Schedule VARCHAR,
                  Date_Start VARCHAR,
                  Date_End VARCHAR,
                  Start_Time VARCHAR,
                  End_Time VARCHAR
                  );
                  ''')
        c.execute('''CREATE TABLE IF NOT EXISTS Event(
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  Name VARCHAR,
                  Type VARCHAR,
                  Date_Start VARCHAR,
                  Date_End VARCHAR
                  );
                  ''')
        connection.commit()

Banco()

class People(Banco):
    def __init__(self, rootframe, frame_people, frame_meeting, frame_event, option_people):
        global count
        self.rootframe = rootframe
        self.frame_people = frame_people
        self.frame_meeting = frame_meeting
        self.frame_event = frame_event
        self.option_people = option_people
        if count%2 == 0:
            self.frame_people.place(x= 0, y= 50)
            self.frame_meeting.place(x= 650, y=50)
            self.frame_event.place(x=975, y=50)
            self.rootframe.place(x=0, y=350)
            #Label's e Entry's
            self.label_name = Label(self.frame_people, text= 'Nome: ', font= '42', bg= 'white')
            self.label_name.place(x= 55, y= 20)
            self.name = Entry(self.frame_people, width= 25)
            self.name.place(x=55, y=50)

            self.label_phone1 = Label(self.frame_people, text='Fone (1): ', font='42', bg= 'white')
            self.label_phone1.place(x=55, y=80)
            self.phone1 = Entry(self.frame_people, width=25)
            self.phone1.place(x=55, y=110)

            self.label_phone2 = Label(self.frame_people, text='Fone (2): ', font='42', bg= 'white')
            self.label_phone2.place(x=55, y=140)
            self.phone2 = Entry(self.frame_people, width=25)
            self.phone2.place(x=55, y=160)
            #botões
            self.button_save = Button(self.frame_people, text= 'Salvar', width= 5, height= 2, bg= 'white', command= self.verification_save)
            self.button_save.place(x= 20, y= 200)

            self.button_search = Button(self.frame_people, text='Pesquisar', width=5, height=2, bg= 'white', command= self.search)
            self.button_search.place(x=130, y=200)

            self.button_erase = Button(self.frame_people, text='Apagar', width=5, height=2, bg= 'white', command= self.delete)
            self.button_erase.place(x=235, y=200)

            count += 1
        else:
            self.frame_people.place(x= 325, y= 50)
            self.frame_meeting.place(x=650, y=50)
            self.frame_event.place(x=975, y=50)
            self.rootframe.place(x= 0, y= 50)
            count += 1

    def delete(self):
        try:
            self.connection = sqlite3.connect('Data.db')
            self.c = self.connection.cursor()
            self.c.execute(f'DELETE FROM People WHERE Name= "{self.namet}";')
        except:
            print('erro')
        finally:
            self.connection.commit()
            self.connection.close()
            self.name.delete(0, 255)
            self.phone1.delete(0, 255)
            self.phone2.delete(0, 255)
            self.button_alter.destroy()

    def verification_save(self):
        self.namet = (self.name.get()).title()
        self.connection = sqlite3.connect('Data.db')
        self.c = self.connection.cursor()
        self.c.execute(f'SELECT * FROM People WHERE Name= "{self.namet}"')
        self.test_name = self.c.fetchall()
        self.connection.close()
        if not self.test_name:
            if self.namet.isdigit() == True or len(self.namet) < 4:
                self.label_name['text'] = 'Nome:* '
                self.label_name['fg'] = 'red'
            else:
                self.label_name['text'] = 'Nome: '
                self.label_name['fg'] = 'black'
            list = [self.phone1.get(), self.phone2.get(), self.label_phone1, self.label_phone2]
            for i in range(2):
                if list[i].isdigit() == False or len(list[i]) > 11 or len(list[0]) < 9:
                    list[i + 2]['text'] = f'Fone ({i + 1}):* '
                    list[i + 2]['fg'] = 'red'
                else:
                    list[i + 2]['text'] = f'Fone ({i + 1}):'
                    list[i + 2]['fg'] = 'black'
            if self.label_name['fg'] == 'black' and self.label_phone1['fg'] == 'black' and self.label_phone2[
                'fg'] == 'black':
                self.save()
        else:
            self.label_name['text'] = 'Usuário já existente'
            self.label_name['fg'] = 'red'

    def save(self):
        try:
            self.connection = sqlite3.connect('Data.db')
            self.c = self.connection.cursor()
            self.c.execute(f'INSERT INTO People(Name, Phone1, Phone2) VALUES("{self.namet}", "{self.phone1.get()}","{self.phone2.get()}");')
        except:
            print('erro')
        finally:
            self.connection.commit()
            self.connection.close()
            self.name.delete(0, 255)
            self.phone1.delete(0, 255)
            self.phone2.delete(0, 255)

    def alter(self):
        self.test_phone = False
        list = [self.phone1.get(), self.phone2.get(), self.label_phone1, self.label_phone2]
        for i in range(2):
            if list[i].isdigit() == False or len(list[i]) > 11 or len(list[0]) < 9:
                list[i + 2]['text'] = f'Fone ({i + 1}):* '
                list[i + 2]['fg'] = 'red'
                self.test_phone = False
            else:
                list[i + 2]['text'] = f'Fone ({i + 1}):'
                list[i + 2]['fg'] = 'black'
                self.test_phone = True
        if self.test_phone == True:
            try:
                self.connection = sqlite3.connect('Data.db')
                self.c = self.connection.cursor()
                self.c.execute(f'UPDATE People SET Name= "{self.namet}", Phone1= "{self.phone1.get()}", Phone2= "{self.phone2.get()}" WHERE Name= "{self.namet}";')
            except:
                print('erro')
            finally:
                self.connection.commit()
                self.connection.close()
                self.name.delete(0, 255)
                self.phone1.delete(0, 255)
                self.phone2.delete(0, 255)
                self.button_alter.destroy()
        self.label_phone1['text'] = f'Fone (2):'
        self.label_phone1['fg'] = 'black'
        self.label_phone2['text'] = f'Fone (2):'
        self.label_phone2['fg'] = 'black'


    def search(self):
        try:
            self.namet = (self.name.get()).title()
            self.name.delete(0, 255)
            self.phone1.delete(0, 255)
            self.phone2.delete(0, 255)

            self.connection = sqlite3.connect('Data.db')
            self.c = self.connection.cursor()
            self.c.execute(f'SELECT * FROM People WHERE Name= "{self.namet}";')
            self.test_search = self.c.fetchall()
            for x in self.test_search:
                self.name.delete(0, 255)
                self.name.insert(END, self.namet)
                self.phone1.insert(END, x[2])
                self.phone2.insert(END, x[3])
        except:
            print('erro search')
        finally:
            self.connection.commit()
            self.connection.close()
        if self.test_search:
            self.button_alter = Button(self.frame_people, text='Alterar', width=5, height=2, bg= 'white', command=self.alter)
            self.button_alter.place(x=130, y=200)
            self.label_name['text'] = 'Nome: '
            self.label_name['fg'] = 'black'
        else:
            self.label_name['text'] = 'Usuário não encontrado'
            self.label_name['fg'] = 'red'

class Meeting():
    def __init__(self, rootframe, frame_meeting, frame_people, frame_event):
        global count
        self.rootframe = rootframe
        self.frame_meeting = frame_meeting
        self.frame_people = frame_people
        self.frame_event = frame_event
        if count % 2 == 0:
            self.frame_meeting.place(x=0, y=50)
            self.frame_people.place(x= 325, y= 50)
            self.frame_event.place(x=975, y=50)
            self.rootframe.place(x=0, y=350)
            #Label's e Entry's
            self.label_name = Label(self.frame_meeting, text='Descrição: ', font='42', bg= 'white')
            self.label_name.place(x=55, y=20)
            self.name = Entry(self.frame_meeting, width=25)
            self.name.place(x=55, y=50)

            self.label_type = Label(self.frame_meeting, text='Pauta: ', font='42', bg= 'white')
            self.label_type.place(x=55, y=80)
            self.type = Entry(self.frame_meeting, width=25)
            self.type.place(x=55, y=110)

            self.label_start = Label(self.frame_meeting, text='Data inicio: ', font='42', bg= 'white')
            self.label_start.place(x=35, y=140)
            self.date_start = Entry(self.frame_meeting, width=10)
            self.date_start.place(x=35, y=160)

            self.label_end = Label(self.frame_meeting, text='Data Fim: ', font='42', bg= 'white')
            self.label_end.place(x=205, y=140)
            self.date_end = Entry(self.frame_meeting, width=10)
            self.date_end.place(x=205, y=160)

            self.label_start_time = Label(self.frame_meeting, text='Hora inicio: ', font='42', bg= 'white')
            self.label_start_time.place(x=35, y=190)
            self.start_time = Entry(self.frame_meeting, width=10)
            self.start_time.place(x=35, y=210)

            self.label_end_time = Label(self.frame_meeting, text='Hora Fim: ', font='42', bg= 'white')
            self.label_end_time.place(x=205, y=190)
            self.end_time = Entry(self.frame_meeting, width=10)
            self.end_time.place(x=205, y=210)

            # Botões
            self.button_save = Button(self.frame_meeting, text='Salvar', width=5, height=2, bg= 'white', command= self.save)
            self.button_save.place(x=20, y=250)

            self.button_search = Button(self.frame_meeting, text='Pesquisar', width=5, height=2, bg= 'white')
            self.button_search.place(x=130, y=250)

            self.button_drop = Button(self.frame_meeting, text='Apagar', width=5, height=2, bg= 'white')
            self.button_drop.place(x=235, y=250)
            count += 1
        else:
            self.frame_meeting.place(x=650, y=50)
            self.frame_people.place(x=325, y=50)
            self.frame_event.place(x=975, y=50)
            self.rootframe.place(x=0, y=50)
            count += 1

    def verification(self):
        self.namet = (self.name.get()).title()
        self.typet = (self.type.get()).title()
        self.connection = sqlite3.connect('Data.db')
        self.c = self.connection.cursor()
        if self.choice == 'save_meeting':
            self.c.execute(f'SELECT * FROM Meeting WHERE Description= "{self.namet}"')
        else:
            self.c.execute(f'SELECT * FROM Event WHERE Name= "{self.namet}"')
        self.test_name = self.c.fetchall()
        self.connection.close()
        if not self.test_name:
            list0 = [self.namet, self.typet, self.label_name, self.label_type, 'Nome:', 'Tipo:']
            for i in range(2):
                if list0[i].isdigit() == True or len(list0[i]) < 5:
                    list0[i+2]['text'] = list0[i+4]
                    list0[i+2]['fg'] = 'red'
                else:
                    list0[i+2]['text'] = list0[i+4]
                    list0[i+2]['fg'] = 'black'
            list = [self.date_start, self.date_end, self.label_start, self.label_end, 'Data inicio', 'Data Fim']
            for i in range(2):
                date = list[i].get()
                if len(date) > 0:
                    if '/' in date:
                        try:
                            day = int(date[:2])
                            mouth = int(date[3:5])
                            if day < 0 or day > 31 or mouth < 0 or mouth > 12 or len(date) != 10:
                                list[i+2]['text'] = list[i+4]+'*'
                                list[i+2]['fg'] = 'red'
                            else:
                                list[i+2]['text'] = list[i+4]
                                list[i+2]['fg'] = 'black'
                        except ValueError:
                            list[i+2]['text'] = list[i+4]+'*'
                            list[i+2]['fg'] = 'red'                    
                    else:
                        try:
                            day = int(date[:2])
                            mouth = int(date[2:4])
                            if day < 0 or day > 31 or mouth < 0 or mouth > 12 or len(date) != 8:
                                list[i + 2]['text'] = list[i + 4] + '*'
                                list[i + 2]['fg'] = 'red'
                            else:
                                list[i + 2]['text'] = list[i + 4]
                                list[i + 2]['fg'] = 'black'
                                list[i].insert(2, '/')
                                list[i].insert(5, '/')
                        except ValueError:
                            list[i + 2]['text'] = list[i + 4] + '*'
                            list[i + 2]['fg'] = 'red'
                     
                else:
                    list[i + 2]['text'] = list[i + 4] + '*'
                    list[i + 2]['fg'] = 'red'

            list = [self.start_time, self.end_time, self.label_start_time, self.label_end_time, 'Hora inicio: ', 'Hora Fim: ']
            for i in range(2):
                self.time = list[i].get()
                if len(self.time) > 0:
                    if ':' in self.time:
                        try:
                            hour = int(self.time[:2])
                            minute = int(self.time[3:5])
                            if hour < 0 or hour > 23 or minute < 0 or hour > 60 or len(self.time) != 5:
                                list[i+2]['text'] = list[i+4]+'*'
                                list[i+2]['fg'] = 'red'
                            else:
                                list[i+2]['text'] = list[i+4]
                                list[i+2]['fg'] = 'black'
                        except ValueError:
                            list[i+2]['text'] = list[i+4]+'*'
                            list[i+2]['fg'] = 'red'
                    else:
                        try:
                            hour = int(self.time[:2])
                            minute = int(self.time[2:4])
                            if hour < 0 or hour > 23 or minute < 0 or hour > 59 or len(self.time) != 4:
                                list[i+2]['text'] = list[i+4]+'*'
                                list[i+2]['fg'] = 'red'
                            else:
                                list[i+2]['text'] = list[i+4]
                                list[i+2]['fg'] = 'black'
                                list[i].insert(2, ':')
                        except ValueError:
                            list[i+2]['text'] = list[i+4]+'*'
                            list[i+2]['fg'] = 'red'
                else:
                    list[i + 2]['text'] = list[i + 4] + '*'
                    list[i + 2]['fg'] = 'red'
            if self.label_name['fg'] == 'black' and self.label_type['fg'] == 'black' and self.label_start['fg'] == 'black' and self.label_end['fg'] == 'black' and self.label_start_time['fg'] == 'black' and self.label_end_time['fg'] == 'black':
                if self.choice == 'save_meeting':
                    return 1
                else:
                    return 2
        else:
            self.label_name['text'] = 'Reunião já existente'
            self.label_name['fg'] = 'red'
        
    def save(self):
        self.choice = 'save_meeting'
        if self.verification() == 1:
            try:
                self.connection = sqlite3.connect('Data.db')
                self.c = self.connection.cursor()
                self.c.execute(f'INSERT INTO Meeting(Description, Schedule, Date_Start, Date_End, Start_Time, End_time) VALUES("{self.namet}", "{self.typet}", "{self.date_start.get()}", "{self.date_end.get()}", "{self.start_time.get()}", "{self.End_Time.get()}");')
            except:
                print('erro oi')
            finally:
                self.connection.commit()
                self.connection.close()
                self.name.delete(0, 255)
                self.type.delete(0, 255)
                self.date_start.delete(0, 255)
                self.date_end.delete(0, 255)
                self.start_time.delete(0, 255)
                self.end_time.delete(0, 255)
    
    def search(self):
        try:
            self.namet, self.typet = (self.name.get()).title(), (self.type.get()).title()
            self.name.delete(0, 255)
            self.type.delete(0, 255)
            self.date_start.delete(0, 255)
            self.date_end.delete(0, 255)

            self.connection = sqlite3.connect('Data.db')
            self.c = self.connection.cursor()
            self.c.execute(f'SELECT * FROM Meeting WHERE Name= "{self.namet}";')
            self.test_search = self.c.fetchall()
            for x in self.test_search:
                self.name.delete(0, 255)
                self.name.insert(END, x[1])
                self.type.insert(END, x[2])
                self.date_start.insert(END, x[3])
                self.date_end.insert(END, x[4])
        except:
            print('erro search')
        finally:
            self.name_b = self.namet
            self.connection.commit()
            self.connection.close()
        if self.test_search:
            self.button_alter = Button(self.frame_event, text='Alterar', width=5, height=2, bg= 'white', command=self.alter)
            self.button_alter.place(x=130, y=200)
            self.label_name['text'] = 'Nome: '
            self.label_name['fg'] = 'black'
        else:
            self.label_name['text'] = 'Reunião não encontrada'
            self.label_name['fg'] = 'red'
    
    def alter(self):
        self.choice = 'alter'
        if self.verification() == 2:
            try:
                self.connection = sqlite3.connect('Data.db')
                self.c = self.connection.cursor()
                self.c.execute(f'UPDATE Meetin SET Name= "{self.name.get().title()}", Type= "{self.type.get().title()}", Date_Start= "{self.date_start.get()}", Date_End= "{self.date_end.get()}" WHERE Name= "{self.name_b}";')
            except:
                print('erro na alteração')
            finally:
                self.connection.commit()
                self.connection.close()
                self.name.delete(0, 255)
                self.type.delete(0, 255)
                self.date_start.delete(0, 255)
                self.date_end.delete(0, 255)
                self.button_alter.destroy()
    
    def delete(self):
        try:
            self.connection = sqlite3.connect('Data.db')
            self.c = self.connection.cursor()
            self.c.execute(f'DELETE FROM Meeting WHERE Name= "{self.namet}";')
        except:
            print('erro')
        finally:
            self.connection.commit()
            self.connection.close()
            self.name.delete(0, 255)
            self.type.delete(0, 255)
            self.date_start.delete(0, 255)
            self.date_end.delete(0, 255)
            self.button_alter.destroy()

class Event():
    def __init__(self, rootframe, frame_event, frame_people, frame_meeting):
        global count
        self.rootframe = rootframe
        self.frame_event = frame_event
        self.frame_people = frame_people
        self.frame_meeting = frame_meeting
        
        #Label's e Entry's
        self.label_name = Label(self.frame_event, text='Nome: ', font='42', bg= 'white')
        self.label_name.place(x=55, y=20)
        self.name = Entry(self.frame_event, width=25)
        self.name.place(x=55, y=50)

        self.label_type = Label(self.frame_event, text='Tipo: ', font='42', bg= 'white')
        self.label_type.place(x=55, y=80)
        self.type = Entry(self.frame_event, width=25)
        self.type.place(x=55, y=110)

        self.label_start = Label(self.frame_event, text='Data inicio: ', font='42', bg= 'white')
        self.label_start.place(x=35, y=140)
        self.date_start = Entry(self.frame_event, width=10)
        self.date_start.place(x=35, y=160)

        self.label_end = Label(self.frame_event, text='Data Fim: ', font='42', bg= 'white')
        self.label_end.place(x=205, y=140)
        self.date_end = Entry(self.frame_event, width=10)
        self.date_end.place(x=205, y=160)

        # Botões
        self.button_save = Button(self.frame_event, text= 'Salvar', width= 5, height= 2, bg= 'white', command= self.save)
        self.button_save.place(x= 20, y= 200)

        self.button_search = Button(self.frame_event, text='Pesquisar', width=5, height=2, bg= 'white', command= self.search)
        self.button_search.place(x=130, y=200)

        self.button_erase = Button(self.frame_event, text='Apagar', width=5, height=2, bg= 'white', command= self.delete)
        self.button_erase.place(x=235, y=200)
        if count % 2 == 0:
            self.frame_meeting.place(x=650, y=50)
            self.frame_people.place(x=325, y=50)
            self.frame_event.place(x=0, y=50)
            self.rootframe.place(x=0, y=350)
            count += 1
        else:
                       
            self.frame_meeting.place(x=650, y=50)
            self.frame_people.place(x=325, y=50)
            self.frame_event.place(x=975, y=50)
            self.rootframe.place(x=0, y=50)
            count += 1

    def verification(self):
        self.namet = (self.name.get()).title()
        self.typet = (self.type.get()).title()
        self.connection = sqlite3.connect('Data.db')
        self.c = self.connection.cursor()
        if self.choice == 'save_meeting':
            self.c.execute(f'SELECT * FROM Meeting WHERE Name= "{self.namet}"')
        else:
            self.c.execute(f'SELECT * FROM Event WHERE Name= "{self.namet}"')
        self.test_name = self.c.fetchall()
        self.connection.close()
        if not self.test_name:
            list0 = [self.namet, self.typet, self.label_name, self.label_type, 'Nome:', 'Tipo:']
            for i in range(2):
                if list0[i].isdigit() == True or len(list0[i]) < 5:
                    list0[i+2]['text'] = list0[i+4]
                    list0[i+2]['fg'] = 'red'
                else:
                    list0[i+2]['text'] = list0[i+4]
                    list0[i+2]['fg'] = 'black'
            list = [self.date_start, self.date_end, self.label_start, self.label_end, 'Data inicio', 'Data Fim']
            for i in range(2):
                date = list[i].get()
                if len(date) > 0:
                    if '/' in date:
                        try:
                            day = int(date[:2])
                            mouth = int(date[3:5])
                            if day < 0 or day > 31 or mouth < 0 or mouth > 12 or len(date) != 10:
                                list[i+2]['text'] = list[i+4]+'*'
                                list[i+2]['fg'] = 'red'
                            else:
                                list[i+2]['text'] = list[i+4]
                                list[i+2]['fg'] = 'black'
                        except ValueError:
                            list[i+2]['text'] = list[i+4]+'*'
                            list[i+2]['fg'] = 'red'
                    else:
                        try:
                            day = int(date[:2])
                            mouth = int(date[2:4])
                            if day < 0 or day > 31 or mouth < 0 or mouth > 12 or len(date) != 8:
                                list[i + 2]['text'] = list[i + 4] + '*'
                                list[i + 2]['fg'] = 'red'
                            else:
                                list[i + 2]['text'] = list[i + 4]
                                list[i + 2]['fg'] = 'black'
                                list[i].insert(2, '/')
                                list[i].insert(5, '/')
                        except ValueError:
                            list[i + 2]['text'] = list[i + 4] + '*'
                            list[i + 2]['fg'] = 'red'
                else:
                    list[i + 2]['text'] = list[i + 4]
                    list[i + 2]['fg'] = 'red'

            if self.label_name['fg'] == 'black' and self.label_type['fg'] == 'black' and self.label_start['fg'] == 'black' and self.label_end['fg'] == 'black':
                if self.choice == 'save_event':
                    return 1
                else:
                    return 2
        else:
            self.label_name['text'] = 'Reunião já existente'
            self.label_name['fg'] = 'red'
        
    def save(self):
        self.choice = 'save_event'
        if self.verification() == 1:
            try:
                self.connection = sqlite3.connect('Data.db')
                self.c = self.connection.cursor()
                self.c.execute(f'INSERT INTO Event(Name, Type, Date_Start, Date_End) VALUES("{self.namet}", "{self.typet}", "{self.date_start.get()}", "{self.date_end.get()}");')
            except:
                print('erro oi')
            finally:
                self.connection.commit()
                self.connection.close()
                self.name.delete(0, 255)
                self.type.delete(0, 255)
                self.date_start.delete(0, 255)
                self.date_end.delete(0, 255)
    
    def search(self):
        try:
            self.namet, self.typet = (self.name.get()).title(), (self.type.get()).title()
            self.name.delete(0, 255)
            self.type.delete(0, 255)
            self.date_start.delete(0, 255)
            self.date_end.delete(0, 255)

            self.connection = sqlite3.connect('Data.db')
            self.c = self.connection.cursor()
            self.c.execute(f'SELECT * FROM Event WHERE Name= "{self.namet}";')
            self.test_search = self.c.fetchall()
            for x in self.test_search:
                self.name.delete(0, 255)
                self.name.insert(END, x[1])
                self.type.insert(END, x[2])
                self.date_start.insert(END, x[3])
                self.date_end.insert(END, x[4])
        except:
            print('erro search')
        finally:
            self.name_b = self.namet
            self.connection.commit()
            self.connection.close()
        if self.test_search:
            self.button_alter = Button(self.frame_event, text='Alterar', width=5, height=2, bg= 'white', command=self.alter)
            self.button_alter.place(x=130, y=200)
            self.label_name['text'] = 'Nome: '
            self.label_name['fg'] = 'black'
        else:
            self.label_name['text'] = 'Reunião não encontrada'
            self.label_name['fg'] = 'red'
    
    def alter(self):
        self.choice = 'alter'
        if self.verification() == 2:
            try:
                self.connection = sqlite3.connect('Data.db')
                self.c = self.connection.cursor()
                self.c.execute(f'UPDATE Event SET Name= "{self.name.get().title()}", Type= "{self.type.get().title()}", Date_Start= "{self.date_start.get()}", Date_End= "{self.date_end.get()}" WHERE Name= "{self.name_b}";')
            except:
                print('erro na alteração')
            finally:
                self.connection.commit()
                self.connection.close()
                self.name.delete(0, 255)
                self.type.delete(0, 255)
                self.date_start.delete(0, 255)
                self.date_end.delete(0, 255)
                self.button_alter.destroy()
    
    def delete(self):
        try:
            self.connection = sqlite3.connect('Data.db')
            self.c = self.connection.cursor()
            self.c.execute(f'DELETE FROM Event WHERE Name= "{self.namet}";')
        except:
            print('erro')
        finally:
            self.connection.commit()
            self.connection.close()
            self.name.delete(0, 255)
            self.type.delete(0, 255)
            self.date_start.delete(0, 255)
            self.date_end.delete(0, 255)
            self.button_alter.destroy()
            
def mouse(event):
    if 's' == str(event.widget)[-2] or 's' == str(event.widget)[-1]:
        x = (str(event.widget)[-1])
        if x == '3':
            Event(rootframe, frame_event, frame_people, frame_meeting)
        elif x == '2':
            Meeting(rootframe, frame_meeting, frame_people, frame_event)
        elif x == 's':
            People(rootframe, frame_people, frame_meeting, frame_event, option_people)

    else:
        pass


count = 0
root = Tk()
root.title('Agenda')
root = root
root.geometry('325x475+900+100')
# root.resizable(False, False)
root['bg'] = '#F8F8FF'

frame_people = Frame(root, width=325, height=300, bg= 'white')
frame_people.place(x=325, y=50)
frame_meeting = Frame(root, width=325, height=300, bg= 'white')
frame_meeting.place(x=650, y=50)
frame_event = Frame(root, width=325, height=300, bg= 'white')
frame_event.place(x=975, y=50)

rootframe = Frame(root, width=325, height=535, bg= '#F8F8FF')
rootframe.place(x= 0, y= 50)


menu = Frame(root, width=325, height=50, bg= 'white')
menu.place(x=0,y=0)

option_people = Canvas(menu, width= 107, height= 50, cursor= 'hand2', bg= '#F8F8FF')
option_people.place(x= 0, y= 0)
img_people = PhotoImage(file='Pessoa.png')
option_people.create_image (55,25,image=img_people)

option_meeting = Canvas(menu, width=107, height=50, cursor='hand2', bg= '#F8F8FF')
option_meeting.place(x= 107, y= 0)
img_meeting = PhotoImage(file='Reunião.png')
option_meeting.create_image (55,25,image=img_meeting)

option_event = Canvas(menu, width=107, height=50, cursor='hand2', bg= '#F8F8FF')
option_event.place(x= 214, y= 0)
img_event = PhotoImage(file='Evento.png')
option_event.create_image (55,25,image=img_event)

root.bind('<Button-1>', mouse)

root.mainloop()