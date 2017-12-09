import socket
import time
import struct

def getCRC(head, data):
    crc = ord(head[0]) ^ ord(head[1])
    for i in data: crc ^= ord(i)
    return [chr(crc)]

pluto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.4.1'
port = 23
pluto.connect((ip, port))
pluto.settimeout(1)

print 'Pluto connected at %s:%d'%(ip, port)

## SEND MSP SET RAW RC
header = ['$', 'M', '<']
header2 = [chr(8), chr(214)] ## Size = 8 | MSP ID = 200
payload = [1000,1000,1000,1000]

payloadBytes = struct.pack('<4H', *payload)
finalPacket = header + header2 + list(payloadBytes) + getCRC(header2, payloadBytes)

print "Sending Packet:"
for i in finalPacket: print ord(i),

for data in finalPacket:
    pluto.send(data)

response = pluto.recv(1024)
print 'MSP IDENT:'
for i in response: print ord(i),


pluto.close()
