from socket import *
import threading
import json
from time import sleep

class Client():
    sock = socket(AF_INET, SOCK_STREAM)
    def __init__(self):
        try:
            self.sock.connect(('localhost', 8012))
            print(self.sock.recv(1024).decode('utf-8'))
            self.usuario = input('\nlogin: ')
            self.senha = input('senha:')
            lista = json.dumps([self.usuario, self.senha])
            self.sock.send(bytes(lista, 'utf-8'))
            # Thread = threading.Thread(target=self.enviarMsg)
            # Thread.start()
            while True:
                data = self.sock.recv(1024)
                if not data:
                    break
                print(str(data, 'utf-8'))
        except:
            print('Não foi possivel concetar a esse servidor :(')
    def enviarMsg(self):
        while True:
            texto = input('')
            mensagem = json.dumps([self.usuario, texto])
            self.sock.send(bytes(mensagem, 'utf-8'))

client = Client()