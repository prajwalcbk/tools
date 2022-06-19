#!/bin/bash

from socket import *
import optparse
from threading import *



def connScan(tg_host,tg_port1):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((tg_host,tg_port1))
        print("[+] %d/tcp Open "% tg_port1)
 #       print(sock.recv(1024))
    except:
        print('[-] %d/tcp Closed '% tg_port1)
    finally:
        sock.close()
def portscan(tg_host,tg_port):
    try:
        tg_ip=gethostbyname(tg_host)
    except:
        print('Unknown host %s'%th_host)
    try:
        tg_name=gethostbyaddr(tg_ip)
        print( "[+] Scan results for :"+tg_name[0])
    except:
        print("[+] Scan results for :"+tg_ip)
    setdefaulttimeout(1)
    for tg_port1 in tg_port:
        t=Thread(target=connScan,args=(tg_host,int(tg_port1)))
        t.start()

def main():
    parser=optparse.OptionParser("Usage of program : " + "-H <target host> -p <target port>")
    parser.add_option("-H",dest='tg_host',type='string',help='specify target host')
    parser.add_option('-p',dest='tg_port',type='string',help='specify taget port separated by commas')
    (options,args)=parser.parse_args()
    tg_host=options.tg_host
    tg_port=str(options.tg_port).split(",")
    if(tg_host==None) | (tg_port[0]==None):
        print(parser.usage)
        exit(0)
    portscan(tg_host,tg_port)

if __name__=="__main__":
    main()
