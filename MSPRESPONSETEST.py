import socket
import time

pluto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.4.1'
port = 23
pluto.connect((ip,port))
pluto.settimeout(1)

print ('Pluto connected at %s:%d'%(ip,port))

## SEND MSP IDENT REQUEST
frameList = ['$', 'M', '<', chr(0), chr(109), chr(109)]
for data in frameList:
    pluto.send(data)

response = pluto.recv(1024)
print 'MSP IDNET'
for i in response: print ord(i),


pluto.close()
