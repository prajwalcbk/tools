#!/usr/bin/python3 


import socket


def banner():
    print('''              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
              $        Scanning the Taget Machine of a specific port            $
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$''')
def retbanner(ip,port):
    try:
        socket.setdefaulttimeout(1)
        print(ip+":"+str(port))
       # print(type(ip),type(port))
        s=socket.socket()#socket.AF_INET,socket.SOCK_STREAM)
        r=s.connect((ip,port))
        print("connected")
        banner=(s.recv(1024).decode('utf-8'))
        return banner
    except Exception as e:
        print(e)
        pass
def main():
    banner()
    print(retbanner("13.227.138.91",111))
    #input1()
def input1():
    ip=input("[*] Enter the Ip Address of the target : > ")
    port=int(input("Enter the Port number in which you have to target : >" ))
    banner=retbanner(ip,port)
    if banner:
        print("[+] "+ip+" : "+banner)

main()
