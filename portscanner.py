import pyfiglet
import sys
import socket
from datetime import datetime 

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
    taget = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + srt(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        result = s.connect_ex((target,port))
    if result == 0:
        print("Port {} is open".format(Port))
    s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
except socket.error:
    print("\ Server not responding !!!")
    sys.exit()
