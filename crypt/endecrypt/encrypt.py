


from cryptography.fernet import Fernet


def generatekey():
    f=open('key.txt','wb')
    key=Fernet.generate_key()
    f.write(key)
    f.close()
def loadkey():
    try:
        f=open('key.txt','rb')
        key=f.read()
        if(key==''.encode()):
            f.close()
            generatekey()
            return loadkey()
#        print('returning the key')
        return key
    except:
#        print('File not found creating the file')
        generatekey()
 #       print('Loading  the file')
        return loadkey()
#        print('Loaded completed')



message=input("Enter the message to encrypt > ")



f=Fernet(loadkey())

encryptmessage=f.encrypt(message.encode())

print(encryptmessage.decode())

