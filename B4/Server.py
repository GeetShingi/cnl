import socket
import os
import threading

class Server:
	clients = []
	def create(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.port = 5000
		self.s.bind(('',self.port))
		print("Socket binded to", str(self.port))
		self.createwindow()
		return

	def createwindow(self):
		print("Chat Messenger Server\n")
		ThreadS = threading.Thread(target = self.sender)
		ThreadR = threading.Thread(target = self.receiver)
		ThreadS.start()
		ThreadR.start()

	def sender(self):
		while True:
			msg = input().encode()
			for i in self.clients:
				self.s.sendto(msg,i)

	def receiver(self):
		while True:
			msg,self.addr = self.s.recvfrom(1024)
			if(self.addr not in self.clients):
				self.clients.append(self.addr)
			else:
				print("Message from ",self.addr,":",str(msg.decode()))
				msg = str(msg.decode())
				msg = msg + "||||" + str(self.addr)
				for i in self.clients:
					if(i != self.addr):
						self.s.sendto(msg.encode(),i)

if __name__ == '__main__':
	server = Server()
	server.create()