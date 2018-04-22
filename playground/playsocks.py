import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7448)
socket.socket = socks.socksocket

# proxies = {
#     'http': 'socks5://127.0.0.1:7448',
#     'https': 'socks5://127.0.0.1:7448'
# }

import requests

resp = requests.get('http://myip.kkcha.com/')
print(resp)

# s = socks.socksocket()

# s.connect(('www.whatismyip.com.tw', 80))
# s.sendall("GET / HTTP/1.1 /r/n/r/n")
# print s.recv(1024)
#
# print(reque)
