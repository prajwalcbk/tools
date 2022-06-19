

#!/usr/bin/python3

from urllib.request import urlopen

import hashlib
from termcolor import colored
import threading
import sys

hshv=input('Enter the hash value >')
passlist=str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read(),'utf-8')



def find(i,f1):
        f1.write(i)
        f1.write('\n')
        
	#hashguess=hashlib.sha1(bytes(i,'utf-8')).hexdigest()
	#if (hshv==hashguess):
	#	print(colored('found '+i,'green'))
	#	sys.exit()
	#else:
	#	print(colored('Not found >'+i,'red'))
f=open('passwords.txt','w')
for i in passlist.split('\n'):
	t=threading.Thread(target=find,args=(i,f))
	t.start()
print(colored('Not found in the link ','red'))
