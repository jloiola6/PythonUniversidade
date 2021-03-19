from socket import *
import threading
import json
import sqlite3

class Banco():
	def __init__(self):
		self.connection = sqlite3.connect('Dados.db')
		self.c = self.connection.cursor()
		self.c.execute('''CREATE TABLE IF NOT EXISTS login(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			login TEXT,
			senha TEXT);
			''')
		self.connection.commit()
		self.connection.close()

	def pesquisar(self, login, senha):
		self.connection = sqlite3.connect('Dados.db')
		self.c = self.connection.cursor()
		self.c.execute(f'''SELECT * FROM login WHERE login= "{login}" AND senha= "{senha}"''')
		if self.c.fetchone() != None:
			return True

class Server():
	sock = socket(AF_INET, SOCK_STREAM)
	connections = []
	nomes = []
	def __init__(self):
		try:
			self.sock.bind(('', 8012))
			self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
			x = int(input('Digite o limite do servidor: '))
			self.sock.listen(x)
			print('Aguardando conexão...')
		except OSError:
			print('Endereço ja esta em uso!')

	def login(self, con, cliente):
		while True:
			try:
				data = con.recv(1024).decode('utf-8')
				data = json.loads(data)
				if banco.pesquisar(data[0], data[1]) == True:
					con.send(bytes(f'Bem vindo {data[0]}\n', 'utf-8'))
					con.send(bytes(f'''
					Qual operação voce deseja realizar?
					1- Pesquisar por amigos
					2- Jogar um jogo
					3- Sei lá mano
					4- Só to enchendo linguiça aqui msm 
					''', 'utf-8'))
				else:
					con.send(bytes(f'Usuário não cadastrado!', 'utf-8'))
					con.send(bytes(f'\nVoce será desconectado por questão de segurança', 'utf-8'))

					print(cliente, 'disconectado')
					self.connections.remove(con)
					con.close()
					break
			except:
				print(cliente, 'disconectado')
				self.connections.remove(con)
				con.close()
				break

	def run(self):
		try:
			while True:
				con,  cliente = self.sock.accept()
				con.send(bytes('Bem vindo ao servidor', 'utf-8'))
				Thread = threading.Thread(target=self.login, args= (con, cliente))
				Thread.start()
				self.connections.append(con)
				print(cliente, 'conectado')
		except OSError:
			pass
banco = Banco()
Server = Server()
Server.run()