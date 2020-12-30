import socket
from IPy import IP

print("     _____           __     _____                                  ")
print("    |  __ \         | |    / ____|                                 ")
print("    | |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __  ")
print("    |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| ")
print("    | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |    ")
print("    |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|    ")  
print("\n")
print("     <<<<<----->= Port Scanner By: IAmFalseBeliefs <=----->>>>>")
print("     <<<<<----->=          Ports Made Easy         <=----->>>>>")
print("<<<<<----->= Use nmap to find version of service running <=----->>>>>")
print("\n")

def check_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(s):
	return s.recv(1024)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.settimeout(float(speed))
		sock.connect((ipaddress, port))
		try:
			banner = get_banner(sock)
			print("[----] Port " + str(port) + " is open running" + str(banner))
		except:
			print("[----] Port " + str(port) + " is open No Banner Avaliable")
	except:
		pass

targets = input("[----] Enter URL or IP address to scan (Split multiple targets by coma): ")
speed = input("[----] Enter speed (suggested 0.5 for most acuracy): ")
range1 = input("[----] Please put number of begining port (ie. 80): ")
print("[====] Add one to ending port to scan to that port so if you want 80 type 81")
range2 = input("[----] Please put number of ending port (ie. 100): ")

def scan(target):
	converted_ip = check_ip(target)
	print("\n " + "     <<<<<----->= Scanning " + str(target) + " <=----->>>>>")
	for port in range(int(range1), int(range2)):
		scan_port(converted_ip, port)

if "," in targets:
	for ip_add in targets.split(","):
		scan(ip_add.strip(" "))
else:
	scan(targets)
