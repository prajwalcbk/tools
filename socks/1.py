from requests import *

r=get("http://icanhazip.com")
print(r.content.decode().strip("\n"))
