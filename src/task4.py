import os

print(os.popen('curl ifconfig.me/ip').read())