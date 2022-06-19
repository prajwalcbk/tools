#!/bin/python3

import sys
import socket
from datetime import datetime
try:
	if len(sys.argv)==4:
		target=socket.gethostbyname(sys.argv[1])
	else:
		print("Invalid syntax of arguements")
		print("syntax: python3 portscanner.py <ip> <starting port> <Ending port>")
		sys.exit()
	print("*"*50)
	print("Scanning the target",target)
	print("Time started :",datetime.now())
	print("*"*50)
	for port in range(int(sys.argv[2]),int(sys.argv[3])):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		r=s.connect_ex((target,port))
                #print("Checking the Connection on port {}".format(port))
		if r==0:
			print("Port {} is open".format(port))
			print(s.recv(1024))

			
		s.close()
except KeyboardInterrupt:
	print("\nExiting the program")
	sys.exit()
except socket.error:
	print("Could not connect to Server")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()


