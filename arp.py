#!/bin/python3

import subprocess 
import tkinter 

command_ip='''arp -a | cut -d " "  -f 2'''
command_mac='''arp -a | cut -d " "  -f 4'''

network_ip=subprocess.check_output(command_ip,shell=True)
network_ip=network_ip.decode("utf-8")

network_mac=subprocess.check_output(command_mac,shell=True)
network_mac=network_mac.decode("utf-8")

network_ip=network_ip.strip()
network_ip=network_ip.split('\n')
ip=[]
for i in network_ip:
	ip.append(i)

network_mac=network_mac.strip()
network_mac=network_mac.split('\n')

def click(frame):
	third=tkinter.Label(frame,text='Two same mac address detected')
	third.pack()


mac=[]
for i in network_mac:
	if(i in mac):
		window=tkinter.Tk()
		
		frame=tkinter.Frame(window)
		frame.pack()
		
		first=tkinter.Label(frame,text='You are been trying to Hack')
		first.pack()	
		
		second=tkinter.Label(frame,text='You are under Man in middle attack')
		second.pack()

		button=tkinter.Button(frame , text='Click to know',command=lambda:click(frame))
		button.pack()

		window.mainloop()
	else:
		mac.append(i)


#window=tkinter.Tk()
#label1=tkinter.Label(window,text='You are under Man in middle attack')
#label1.pack()

#frame=tkinter.Frame(window)
#frame.pack()

#first=tkinter.Label(frame,text='You are been trying to Hack')
#first.pack()	
#second=tkinter.Label(frame,text='You are under Man in middle attack')
#second.pack()

#window.mainloop()



print(ip)
print(mac)

