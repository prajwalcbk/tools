import socks
import socket
import requests

socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",9050)
socket.socket=socks.socksocket
r=requests.get("http://icanhazip.com")
print(r.content)




socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",9050)
socket.socket=socks.socksocket
r=requests.get("http://icanhazip.com")
print(r.content)
