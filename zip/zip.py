import zipfile
from termcolor import colored
import sys
zipped=input("Enter the Name of zipped folder=> ")
obj=zipfile.ZipFile(zipped)
filed=input("Enter the path of passwords file=> " )
file=open(filed,'r')
for passwords in file.readlines():
    passwords=passwords.strip("\n").strip("\r")
    passwords='ctflag'+passwords
    try:
        obj.extractall(pwd=bytes(passwords,'utf-8'))
        print(colored("[+]password found => "+passwords,'green'))
        sys.exit(0)
    except Exception as e:
        print(colored("[-] Trying for password >"+passwords,'red'))


