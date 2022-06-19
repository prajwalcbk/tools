

#!/usr/bin/python3

from urllib.request import urlopen

import hashlib
from termcolor import colored
import threading
import sys

hshv=input(colored('Enter the hash value >','yellow'))
passlist=str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read(),'utf-8')


t1=False
def find(i,f1):
    global t1
    hashguess=hashlib.md5(bytes(i,'utf-8')).hexdigest()
    if(hshv==hashguess):
        print(colored('[ + ]found '+i,'green'))
        t1=True
    else:
        print(colored('[-]Not found >'+i,'red'))
        return False
for i in passlist.split('\n'):
    if(t1==True):
        break
    t=threading.Thread(target=find,args=(i,'f'))
    t.start()
if(not t1):
    print(colored('Not found in the link ','red'))
