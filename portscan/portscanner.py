#!/bin/python3

import sys
from socket import *
from termcolor import colored
from datetime import datetime
print(colored('''                        :::::::::::::::::::::::::::::::::::::::::::::::::::
                        :             Port Scanner                        :
                        :::::::::::::::::::::::::::::::::::::::::::::::::::''','yellow'))
try:
        ip_host=input("Enter the name of website or IP Address :")
        sp=int(input("Enter the starting Port Number :"))
        ep=int(input("Enter the ending Port Number :"))
        target=gethostbyname(ip_host)
        print(colored('''                _________________________________________________________________________________
               |                                                                                 |
               |                                                                                 |
               |                                                                                 |
               |        ***  Scanning the target '''+target+''' ***                              | 
               |                                                                                 |
               |                                                                                 |
               |_________________________________________________________________________________|''','green'))
        
        print(colored("Time started :"+str(datetime.now()),'blue'))
        for port in range(sp,ep):
            s=socket(AF_INET,SOCK_STREAM)
            setdefaulttimeout(1)
            r=s.connect_ex((target,port))
            #print("Checking the Connection on port {}".format(port))
            if r==0:
                print(colored("Port "+str(port)+"is open ",'red'))
                s.close()
except KeyboardInterrupt:
	print(colored("Exiting the program",'red'))
	sys.exit()
except error:
	print(colored("Could not connect to Server",'red'))
	sys.exit()
except gaierror:
	print(colored("Hostname could not be resolved",'red'))


