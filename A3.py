import os
import math

def calc_class(inp):
	if(int(inp[0]) < 127):
		return 'A'
	elif(int(inp[0]) >=128 and int(inp[0]) < 192):
		return 'B'
	elif(int(inp[0]) >=192 and int(inp[0]) < 224):
		return 'C'
	else:
		return 'D'

def calc_subnet(inp):
	ip = ""
	if inp is 'A':
		ip = ip + "255.0.0.0"
	elif inp is 'B':
		ip = ip + "255.255.0.0"
	elif inp is 'C':
		ip = ip + "255.255.255.0"
	return ip

def new_subnet(sub,ones,ip_class):
	temp = sub.split('.')
	count = 0
	for i in range(7,7-ones,-1):
		count = count + 2**i
	if ip_class is 'A':
		i = 1
	elif ip_class is 'B':
		i = 2
	else:
		i = 3
	temp[i] = str(count)
	string = temp[0] + '.' + temp[1] + '.' + temp[2] + '.' + temp[3]
	return string

def strtend(ones,num):
	div = 2**ones
	temp = 256/div
	start = []
	end = []
	for i in range(num):
		start.append(int(temp*i))
		end.append(int(temp*(i+1) - 1))

	print(start)
	print(end)
	return 

def check_subnet(ip,sub,ip1):
	res1 = []
	res2 = []
	ip = ip.split('.')
	ip1 = ip1.split('.')
	sub = sub.split('.')
	flag = 0
	for i in range(4):
		temp1 = int(ip[i]) & int(sub[i])
		temp2 = int(ip1[i]) & int(sub[i])

		res1.append(temp1)
		res2.append(temp2)
		if temp1 != temp2:
			flag = 1
	print(res1)
	print(res2)
	return flag


ip =str(input("Enter IP address"))
print(ip)
final_ip = ip.split('.')
print(final_ip)
ip_class = calc_class(final_ip)
print(ip_class)
subnet = calc_subnet(ip_class)
print(subnet)
num = int(input("Enter number of subnets"))
print(num)
ones = math.ceil(float(math.log(num,2)))
print(ones)
sub = new_subnet(subnet,ones,ip_class)
print(sub)
strtend(ones,num)
#os.system('sudo ifconfig wlp60s0 %s netmask %s'%(ip , sub))
ip1 =str(input("Enter IP address to connect"))
print(ip1)
ans = check_subnet(ip,sub,ip1)
if ans is 0:
	print('The new IP entered is in the same subnet')
if ans is 1:
	print('The new IP entered is not in the same subnet')

# os.system("ifconfig")

os.system("ping %s"%(ip1))
