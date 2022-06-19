import sys
import time



i=0
while(i<100):
    print("\rValue of i is "+str(i),flush=True,end=''),
    sys.stdout.flush()
    i=i+5
    time.sleep(1)
