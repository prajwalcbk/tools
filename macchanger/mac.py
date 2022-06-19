import subprocess
import optparse
from termcolor import colored

def change_mac(interface,new_mac):
    print(colored("[$] Changing MAC for interface "+ interface + " to "+ new_mac,'yellow'))
    before_change=subprocess.check_output(['ifconfig',interface])
    subprocess.call(["ifconfig",interface ,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    after_change=subprocess.check_output(['ifconfig',interface])
    if(after_change==before_change):
        print(colored('[!][-] Falied to change the MacAddress','red'))
    else:
        print(colored('[+] Successfully the MacAddress is Changed','green'))

def input_parse():
    parser=optparse.OptionParser('Usage of the program : python3 mac.py -i <interface> -m <new_mac>')
    parser.add_option("-i",dest="interface",type='string',help="Specify interface to change MAC")
    parser.add_option("-m",dest="mac",type='string',help="Specify the new MAC to change")
    options,arguments=parser.parse_args()
    return options.interface ,options.mac

#interface=input("interface > ")
#mac=input("MAC > ")
try:
 interface,mac=(input_parse())
 change_mac(interface,mac)
except Exception as e:
    print(e)

