
#!/bin/python3
import requests


def convert(b):
    bs=str(b.content)
    bs=bs.split("\\n")
    for i in bs:
        print(i)


r=requests.get("https://www.hackthebox.eu/invite")
convert(r)

exit()
user_name=input("Enter the User-Agent > :")
myhead={'User-Agent':user_name}
r=requests.get("http://httpbin.org/headers",headers=myhead)
convert(r)


user_name=input("Enter the User-Agent > :")
host_name=input("Enter the host name > :")
myhead={'User-Agent':user_name,'Host':host_name}
r=requests.get("http://httpbin.org/headers",headers=myhead)
convert(r)
