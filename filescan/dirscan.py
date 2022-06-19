#!/usr/bin/python3

import requests
from termcolor import colored
def request(url):
    try :
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass


target_url=input("[*] Enter the Target URL > ")
file_name=input("[*] Enter the path of the fie > ")

file = open(file_name,"r")
for line in file:
    word=line.strip()
    full_url=target_url+"/"+word
    response=request(full_url)
    if response:
        print(colored("[+] Discovered Directory at this link : "+ full_url,'green'))

