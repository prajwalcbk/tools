

from argparse import *
#from optparse imort *
from termcolor import colored
from scapy.all import *
import time


def a():
    


    #parser=Optionparser('')
    #parser.add_option()

    parser=ArgumentParser(colored('Usage of the Program ','green')+(colored(' pyhton3 iptcpraw.py -s <ip> -sp <sport> -t <ip> -tp <tport> -l <load> \n','red')))
    parser.add_argument('-t',dest='target',help='Target IP Address')
    parser.add_argument('-s',dest='source',help='source IP address remember to change like spoof')
    parser.add_argument('-tp',dest='tport',help='Destination port number u need to attak')
    parser.add_argument('-sp',dest='sport',help='Source portnumber')
    parser.add_argument('-l',dest='load',help='load message of TCP header')
    return parser.parse_args()

def sp(source,target,tport,spor,load):
    ip=IP(src=source,dst=target)
    tcp=TCP(sport=int(spor),dport=int(tport))
    i=ip/tcp
    raw=Raw(load=load)
    ip=i/raw
    for i in range(10):
        send(ip)
        print(colored('                 NUmber of Packets Sent>'+str(i+1),'red'),flush=True,end='')

r=a()
try:
    sp(r.source,r.target,r.tport,r.sport,r.load)
    print('')
except Exception as e:
    print(colored(e,'red'))
    print(colored('KEY INTERRUPTED','red'))




