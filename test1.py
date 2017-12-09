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
header2 = [chr(16), chr(200)] ## Size = 8 | MSP ID = 200
payload = [1000]*3 + [0] + [0]*3 + [1500] ## ARM drone

payloadBytes = struct.pack('<8H', *payload)
finalPacket = header + header2 + list(payloadBytes) + getCRC(header2, payloadBytes)

print "Sending Packet:"
for i in finalPacket: print ord(i),
while(1):
      for data in finalPacket:
       pluto.send(data)
#time.sleep(0.5)
#print("data")


#response = pluto.recv(1024)
#print 'MSP IDENT:', response

pluto.close()

