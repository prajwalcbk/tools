

from cryptography.fernet import Fernet

def loadkey():
    f=open('key.txt','rb')
    key=f.read()
    if(key==''.encode()):
        generatekey()
        loadkey()
    f.close()
    return key

encryptmsg=input('Enter the encrypted message > ')
encryptmsg=encryptmsg.encode()


f=Fernet(loadkey())

print(f.decrypt(encryptmsg).decode())


