from pynput.keyboard import Key, Listener
import time
import os
import random
import requests
import socket

sourcecode =requests.get('http://192.168.43.25/login.php').text
privateip=socket.gethostbyname(socket.gethostname())
user=os.path.expanduser('~')   #.split('\\')[0]   depends upon the windows are linux
datetime=time.ctime(time.time())

def print1():
	print('IP_Address :'+privateip)	
	print('Source code :\n'+sourcecode)
	print('Date and time :'+datetime)
	print('User :'+user)

print1()
