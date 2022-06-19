import time
i=0
try:
    while(i<100):
        print("\r"+str(i),flush=True,end='')
        i+=1
        time.sleep(0.1)
except:
    print('')

