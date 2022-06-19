#!/usr/bin/python3


import scapy.all as scapy
import argparse


def scan(ip):
	scapy.arping(ip)

#scan("192.168.43.0/24")


def scan1(ip):
	arp_packet=scapy.ARP()
	arp_packet.show()

#scan1("192.168.43.1/24")


def scan2(ip):
	arp_packet=scapy.ARP(pdst=ip)
	broadcast_packet=scapy.Ether()
	broadcast_packet.show()

#scan2("192.168.43.1/24")


def scan3(ip):
	arp_packet=scapy.ARP(pdst=ip)
	broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_packet=broadcast_packet/arp_packet
	answered_packet=scapy.srp(arp_broadcast_packet,timeout=1,verbose=False)[0]
	for element in answered_packet:
            print(element)
            print()
scan3("192.168.43.1/24")

def get_arguments():
	parser=argparse.ArgumentParser()
	parser.add_argument("-t",dest="target",help="Specify the IP range or IP")
	options=parser.parse_args()
	return options

def scan4(ip):
	arp_packet=scapy.ARP(pdst=ip)
	broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_packet=broadcast_packet/arp_packet
	answered_packet=scapy.srp(arp_broadcast_packet,timeout=1,verbose=False)[0]
	client_list=[]
	for element in answered_packet:
		client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
		client_list.append(client_dict)
	return client_list

def print_result(scan_list):
	print("IP\t\t\t\tMAC\n--------------------------------------------")
	for client in scan_list:
		print(client['ip']+"\t\t" + client['mac'])

options=get_arguments()

result_scan=scan4(options.target)

#print_result(result_scan)


