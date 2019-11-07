import os
import threading
import socket

class Client:
	def create(self):
		self.ip = "127.0.0.1"
		self.port = 5000
		self.c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		print("Socket Created Successfully")
		self.c.sendto(('').encode(),(self.ip,self.port))
		self.createwindow()
		return

	def createwindow(self):
		os.system("clear")
		print("Chat Messenger Client\n")
		ThreadS = threading.Thread(target = self.sender)
		ThreadR = threading.Thread(target = self.receiver)
		ThreadS.start()
		ThreadR.start()

	def sender(self):
		while True:
			msg = input().encode()
			self.c.sendto(msg,(self.ip,self.port))

	def receiver(self):
		while True:
			msg,addr = self.c.recvfrom(1024)
			if("||||" in msg.decode()):
				msg,addr = msg.decode().split("||||")
				print("Msg from ",str(addr),":",str(msg))
			else:
				print("Msg from ",str(addr),":",str(msg.decode()))

if __name__ == "__main__":
	client = Client()
	client.create()
	# client.createwindow()

