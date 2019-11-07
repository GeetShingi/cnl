import csv
ip = 0
choice = int(input("Enter Protocol\n1. IP\n2. TCP\n3. UDP\n4. Ethernet\n"))
if choice is 1:
	ch = "ICMPv6"
elif choice is 2:
	ch = "TCP"
elif choice is 3:
	ch = "UDP"
else:
	ch = "ARP"
print("Sr.No\t\tTime\t\t\tSource\t\t\tDestination\tProtocol\tLength\tInfo")
with open('data.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if ch in row[4]:
			ip = ip + 1
			print(ip,"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])

print("There are total",ip,"packets of",ch,"protocol")
