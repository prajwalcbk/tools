#!/usr/bin/python3

from crypt import crypt
from termcolor import colored
from threading import Thread




def crack(user,cryptword):
    salt=cryptword[:2]
    dicfile=open('dict.txt','r')
    for word in dicfile.readlines():
        word=word.strip('\n')
        cryptpass=crypt(word,salt)
        if(cryptpass==cryptword):
            print(colored("[+] Password found for the user "+user+" which is >"+word,'green'))

def main():
    passfile=open('pass.txt','r')
    for line in passfile.readlines():
        if ':' in line:
            user=line.split(':')[0]
            cryptword=line.split(':')[1].strip(' ').strip('\n')
            print(colored("[-] Cracking the password for the user  > "+user,'red'))
            t=Thread(target=crack,args=(user,cryptword))
            t.start()



main()
