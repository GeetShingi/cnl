import socket
import os
import sys
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buff = 1024
file_name = sys.argv[1]

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(("Hello").encode(), (UDP_IP,UDP_PORT))
sock.sendto(file_name.encode(), (UDP_IP,UDP_PORT))
print("Sending file ",file_name)
f = open(file_name,"r")
data = f.read(buff)
while(data):
	if(sock.sendto(data.encode(),(UDP_IP,UDP_PORT))):
		data = f.read(buff)
		time.sleep(0.02)

sock.close()
f.close()