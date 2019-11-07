import socket
import select

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
timeout = 3

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
	data,addr = sock.recvfrom(1024)
	print("Msg:", data.decode())
	data,addr = sock.recvfrom(1024)
	print("Filename:", data.decode())
	file_name = data.decode()
	f = open(file_name,"wb")
	while True:
		ready = select.select([sock],[],[],timeout)
		if ready[0]:
			data,addr = sock.recvfrom(1024)
			f.write(data)
		else:
			print(file_name," Finish")
			f.close()
			break
	break

sock.close()


