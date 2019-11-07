import os
import socket
import threading

class Server:
	client = any
	def create(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.port = 5000
		self.s.bind(('',self.port))
		print("Socket binded to ",str(self.port))
		self.createwindow()
		return

	def createwindow(self):
		print("User 1\n")
		ThreadS = threading.Thread(target = self.sender)
		ThreadR = threading.Thread(target = self.receiver)
		ThreadS.start()
		ThreadR.start()

	def sender(self):
		while True:
			msg = input().encode()
			self.s.sendto(msg,self.client)

	def receiver(self):
		while True:
			msg,self.addr = self.s.recvfrom(1024)
			if(self.addr != self.client):
				self.client = self.addr7
				print("HELLLLO")
			else:
				print("Message from User 2 : ",str(msg.decode()))

if __name__ == '__main__':
	server = Server()
	server.create()

