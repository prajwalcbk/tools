import os
import socket
import sys


def retbanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		print(ip,port)
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,port))
		print("connected")
		banner=(s.recv(1024))
		return banner
	except Exception as e:
	#	print(e)
		pass

def vuln(banner,filename):
	f=open(filename,'r')
	for line in f.readlines():
		if line.strip("\n") in banner:
			print("[+] Server is Vulnerable : "+banner.strip("\n"))

def main():
	if len(sys.argv)==2:
		filename=sys.argv[1]
		if not os.path.isfile(filename):
			print("[-] File does not exists")
			sys.exit()
		if not os.access(filename,os.R_OK):
			print("[-] permission denied ")
			sys.exit()
	else:
		print("[-] Usage : "+str(sys.argv[0]) +" <vuln filename>")
		sys.exit()
	portlist=[22,21,25,80,110,443,445]
	for x in range(24,25):
		ip='192.168.43.'+str(x)
		for port in portlist:
                    banner=retbanner(ip,port)
                    print(banner)
                    if banner:
                        print("[+] "+ ip + '/' +str(port) + " : "+banner)
                        vuln(banner,filename)
main()
