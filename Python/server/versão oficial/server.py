from socket import *
import threading
import json

class Server():
	sock = socket(AF_INET, SOCK_STREAM)
	connections = []
	nomes = []
	def __init__(self):
		try:
			self.sock.bind(('', 8011))
			self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
			x = int(input('DIgite o limite do servidor: '))
			self.sock.listen(x)
			print('Aguardando conexão...')
		except OSError:
			print('Endereço ja esta em uso!')

	def atualizacao(self, con, cliente):
		con.send(bytes(f'\n{len(self.connections)} online', 'utf-8'))
		while True:
			try:
				data = con.recv(1024).decode('utf-8')
				data = json.loads(data)
			
				for connection in self.connections:
					teste = str(connection)
					if str(cliente[1]) in teste:
						pass
					else:
						connection.send(bytes(f'{data[0]}: {data[1]}', 'utf-8'))
			except:
				print(cliente, 'disconectado')
				self.connections.remove(con)
				con.close()
				for connection in self.connections:
					teste = str(connection)
					if str(cliente[1]) in teste:
						connection.send(bytes(f'Usuário desconectado', 'utf-8'))
				break

	def run(self):
		try:
			while True:
				con,  cliente = self.sock.accept()
				con.send(bytes('Bem vindo ao servidor', 'utf-8'))
				Thread = threading.Thread(target=self.atualizacao, args= (con, cliente))
				Thread.start()
				self.connections.append(con)
				print(cliente, 'conectado')
		except OSError:
			pass

Server = Server()
Server.run()